# Copyright (c) 2025, John and contributors
# For license information, please see license.txt

import frappe ,json
from frappe import _
from frappe.model.document import Document
from erpnext.controllers.queries import get_match_cond
from frappe.model.workflow import apply_workflow
from frappe.utils import now_datetime, get_url_to_form, getdate

class VehicleRental(Document):
	def validate(self):
		if not self.vehicle:
			frappe.throw("Vehicle is required")
		rental_check =  frappe.db.get_list("Vehicle Rental", filters={"vehicle": self.vehicle, "docstatus": 1 , "start_date": ["<=", self.end_date], "end_date": [">=", self.start_date], "name": ["!=", self.name], "status": ["in", ("Overdue","On Rent","Reserved","Draft","Extended")]}, limit=1)
		# rental_check = frappe.db.sql("""select name,ADDTIME(start_date,'-0 0:30:0.0') as start_date,ADDTIME(end_date,'-0 0:30:0.0') as end_date from erpnextdb.`tabVehicle Rental` 
		# where vehicle =%(vehicle)s
		# and status in ('Overdue','On Rent','Reserved','Draft','Extended')
		# and ( ADDTIME(start_date,'-0 0:30:0.0')   BETWEEN %(start_date)s and %(end_date)s
		# or ADDTIME(end_date,'-0 0:30:0.0')  BETWEEN %(start_date)s and %(end_date)s )
		# and name != %(name)s""",{'vehicle':self.vehicle,'start_date':self.start_date,'end_date':self.end_date,'name':self.name},as_dict=True)
		if len(rental_check) > 0:
			frappe.throw("Vehicle {0} is already rented for the selected dates. from {1} to {2}".format(self.vehicle, rental_check[0].start_date, rental_check[0].end_date))
	def validate_from_to_dates(self, from_date_field, to_date_field):
		if not self.get(from_date_field) or not self.get(to_date_field):
			frappe.throw(f"{from_date_field} and {to_date_field} are required")

		if self.get(from_date_field) > self.get(to_date_field):
			frappe.throw(f"{from_date_field} must be before {to_date_field}")

	def before_save(self):
		self.user_id = frappe.session.user

	def before_update_after_submit(self):
		if self.workflow_state == 'Return':
			mileage = frappe.db.get_value('Vehicle Master', self.vehicle, 'total_mileage')
			mileage = mileage if mileage else 0
			frappe.new_doc("Vehicle History").update({
				"parent": self.vehicle,
				"parenttype": 'Vehicle Master',
				"parentfield": "vehicle_history",
				'from_time': self.start_date,
				'to_time': self.end_date,
				'mileage': int(mileage) + int(self.end_mileage) - int(self.start_mileage)
			}).insert(ignore_permissions=True)

			frappe.db.set_value('Vehicle Master', self.vehicle, 'total_mileage', int(mileage) + int(self.end_mileage) - int(self.start_mileage), update_modified=True)
			# apply_workflow(self, 'Return')
	@frappe.whitelist()
	def rent_return(self):
		self.return_date = frappe.utils.nowdate()
		self.status = "Returned"

	@frappe.whitelist()
	def rent_extend(self, new_end_date):
		self.end_date = new_end_date
		self.status = "Extended"

	@frappe.whitelist()
	def rent_cancel(self):
		self.status = "Cancelled"

	@frappe.whitelist()
	def rent_start(self):
		self.status = "On Rented"

	@frappe.whitelist()
	def rent_reserved(self):
		self.status = "Reserved"

	@frappe.whitelist()
	def rent_unreserve(self):
		self.status = "Draft"


# import equipment_rental.equipment_rental.doctype.vehicle_rental.vehicle_rental.get_events
@frappe.whitelist()
def get_events(start=None, end=None, filters=None):
	"""Returns events for Gantt / Calendar view rendering.
	:param start: Start date-time.
	:param end: End date-time.
	:param filters: Filters (JSON).
	"""	
	start_date = start
	end_date = end
	filters = json.loads(filters) if filters else {}
	from frappe.desk.calendar import get_event_conditions

	conditions = get_event_conditions("Vehicle Rental", filters)

	return frappe.db.sql(
		"""select 
			`tabVehicle Rental`.name as name,
			`tabVehicle Rental`.status,
			start_date as start_date, end_date as end_date,
			CONCAT(`tabVehicle Rental`.rental_purpose, ' (',
				ROUND(TIME_TO_SEC(TIMEDIFF(`tabVehicle Rental`.end_date, `tabVehicle Rental`.start_date))/3600, 1), '시간)') as title,
			CASE 
				WHEN `tabVehicle Rental`.status = 'On Rent' THEN '#2196f3'
				WHEN `tabVehicle Rental`.status = 'Reserved' THEN '#ff9800'
				WHEN `tabVehicle Rental`.status = 'Overdue' THEN '#f44336'
				WHEN `tabVehicle Rental`.status = 'Draft' THEN '#9e9e9e'
				WHEN `tabVehicle Rental`.status = 'Extended' THEN '#4caf50'
				WHEN `tabVehicle Rental`.status = 'Return' THEN '#607d8b'
				ELSE '#607d8b'
			END as color
		from `tabVehicle Rental`
		where docstatus < 2
		and status in ('Overdue','On Rent','Reserved','Draft','Extended','Return')
			and (start_date <= %(end_date)s and end_date >= %(start_date)s) {conditions} {match_cond}
		""".format(conditions=conditions, match_cond=get_match_cond("Vehicle Rental")),
		{"start_date": start_date, "end_date": end_date},
		as_dict=True,
		update={"allDay": 0},
	)

# bench execute equipment_rental.equipment_rental.doctype.vehicle_rental.vehicle_rental.extend_rental --krwargs {'docname':'VEHICLE_RENTAL_001','new_end_date':'2023-12-31'}
@frappe.whitelist()
def extend_rental(**kwargs):
	print(kwargs.get("doc"))
	doc = json.loads(kwargs.get("doc"))
	print(doc)
	vehicle_rental = frappe.get_doc("Vehicle Rental", doc.get("name"))
	print(vehicle_rental)
	vehicle_rental.end_date = kwargs.get("new_end_date")
	vehicle_rental.status = "Extended"
	vehicle_rental.save()
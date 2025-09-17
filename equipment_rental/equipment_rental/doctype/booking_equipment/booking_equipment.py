# Copyright (c) 2025, John and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BookingEquipment(Document):

	def validate(self):
		self.validate_equipment_availability()
		self.validate_dates()

	def validate_dates(self):
		if self.from_date >= self.to_date:
			frappe.throw("From date must be before To date.")

		if self.from_date < frappe.utils.nowdate():
			frappe.throw("From date cannot be in the past.")

		if self.to_date < frappe.utils.nowdate():
			frappe.throw("To date cannot be in the past.")

	def validate_equipment_availability(self):
		if self.equipment:
			# equipment_doc = frappe.get_doc("Equipment Master", self.equipment)
			booking_list = frappe.db.sql("""
select tbe.name from `tabBooking Equipment` tbe 
where tbe.equipment =%(equipment)s
and (tbe.from_date BETWEEN %(from_date)s and %(to_date)s
or tbe.to_date BETWEEN %(from_date)s and %(to_date)s )
and tbe.name != %(name)s
""",{'equipment':self.equipment,'from_date':self.from_date,'to_date':self.to_date,'name':self.name},as_dict=True)
			if len(booking_list) > 0:
				for booking in booking_list:
					print(booking.name)
				frappe.throw(f"Equipment {self.equipment} is already booked for the selected dates."	)

frappe.views.calendar["Vehicle Rental"] = {
	field_map: {
		start: "start_date",
		end: "end_date",
		id: "name",
		title: "title",
		allDay: "allDay",
		color: "color",
	},
	// order_by: "scheduled_on",
	gantt: true,
	get_events_method: "equipment_rental.equipment_rental.doctype.vehicle_rental.vehicle_rental.get_events",
};

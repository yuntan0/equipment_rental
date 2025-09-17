
frappe.views.calendar["Booking Equipment"] = {
	field_map: {
		start: "from_date",
		end: "to_date",
		id: "name",
		title: "equipment_name",
		allDay: "allDay",
	},
	gantt: false,
	filters: [
		{
			fieldtype: "Link",
			fieldname: "equipment_master",
			options: "Equipment Master",
			label: __("Equipment"),
		},
	],
	get_events_method: "frappe.desk.calendar.get_events",
};
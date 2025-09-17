// Copyright (c) 2025, John and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle Rental", {
	refresh(frm) {
        frm.add_custom_button(__(frm.doc.vehicle), () => {
                frappe.set_route("Form", 'Vehicle Master', frm.doc.vehicle);
        });  
        frm.add_custom_button(__('Extend Rental'), () => {
                frappe.call({
                        method: "equipment_rental.equipment_rental.doctype.vehicle_rental.vehicle_rental.extend_rental",
                        args: {
                                docname: frm.doc.name,
                                new_end_date: frm.doc.end_date
                        },
                        callback: function (r) {
                                if (r.message) {
                                        frappe.show_alert(__('Rental extended successfully'));
                                        frm.reload_doc();
                                }
                        }
                });
        });  
	},
});

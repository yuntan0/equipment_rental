// Copyright (c) 2025, John and contributors
// For license information, please see license.txt

frappe.ui.form.on("Equipment Master", {
	refresh(frm) {
            frm.add_custom_button(__("Rent Equipment"), function() {
                
                // frappe.call({
                //     method: "equipment_rental.api.get_rental_details",
                //     args: {
                //         equipment_name: frm.doc.name
                //     },
                //     callback: function(response) {
                //         console.log(response);
                //         if (response.message) {
                //             frappe.msgprint(__("Equipment has been rented successfully."));
                //             frm.reload_doc();
                //         } else {
                //             frappe.msgprint(__("Failed to rent equipment."));
                //         }
                //     }
                // });
                frappe.db.get_doc("Equipment Master", frm.doc.name).then(doc => {
                    console.log(doc);
                });
            });
        },
});

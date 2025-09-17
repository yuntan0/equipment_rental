frappe.listview_settings["Vehicle Rental"] = {
    onload: function (listview) {
        listview.page.add_inner_button(__('New Vehicle Rental'), function () {
            frappe.set_route('Form', 'Vehicle Rental', 'New');

        });
        listview.page.add_action_item(__('Mass Extend'), function() {
            const rentals = listview.get_checked_items();
            console.log(rentals);
            array = [];
            rentals.forEach(element => {
                if(element.status == 'Returned'){
                    array.push(element.name);
                    console.log(element);
                }
                
            });
            console.log(array);
            // if (rentals.length === 0) {
            //     frappe.msgprint(__('Please select at least one rental to extend.'));
            //     return;
            // }
            // const new_end_date = prompt(__('Enter new end date'), '');
            // if (!new_end_date) {
            //     return;
            // }
            // frappe.call({
            //     method: "equipment_rental.equipment_rental.doctype.vehicle_rental.vehicle_rental.extend_rental",
            //     args: {
            //         rentals: rentals,
            //         new_end_date: new_end_date
            //     },
            //     callback: function (r) {
            //         if (r.message) {
            //             frappe.show_alert(__('Rentals extended successfully'));
            //             listview.refresh();
            //         }
            //     }
            // });
        });
    }
};
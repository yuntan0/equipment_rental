import frappe




# bench execute equipment_rental.api.get_rental_details --kwargs "{'equipment_name': '250820-000001'}"
@frappe.whitelist()
def get_rental_details(**kwargs):
    print(kwargs)
    equipment_name = kwargs.get("equipment_name")
    print(equipment_name)
    rental = frappe.get_doc("Equipment Master", equipment_name)
    # rental = frappe.get_doc("Equipment Rental", equipment_name)
    print(rental)
    return rental
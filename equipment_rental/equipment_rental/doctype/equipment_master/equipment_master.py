# Copyright (c) 2025, John and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EquipmentMaster(Document):
	pass



@frappe.whitelist()
def get_rental_details(equipment_name):
    print(equipment_name)
    rental = frappe.get_doc("Equipment Rental", equipment_name)
    print(rental)
    return rental

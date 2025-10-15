import frappe

#bench execute equipment_rental.tasks.daily_task
@frappe.whitelist()
def daily_task():
    frappe.log("Running daily task")

#bench execute equipment_rental.tasks.rental_reminder --kwargs  "{'email':'test@test.com' ,'docname':'OFF-250421000012' }"
@frappe.whitelist()
def rental_reminder(**kwargs):
    reminder_list = frappe.db.sql("""select name, party_type, party, start_date, end_date 
        from erpnextdb.`tabVehicle Rental` where end_date = CURDATE() + INTERVAL 1 DAY 
        and status = 'On Rent' """, as_dict=1)
    frappe.log("Sending rental reminder emails")
    recipients = []
    for reminder in reminder_list:
        if reminder.get("party_type") == "Customer":
            customer = frappe.get_doc("Customer", reminder.get("party"))
            if customer.email_id:
                recipients.append(customer.email_id)
        elif reminder.get("party_type") == "Supplier":
            supplier = frappe.get_doc("Supplier", reminder.get("party"))
            if supplier.email_id:
                recipients.append(supplier.email_id)
        elif reminder.get("party_type") == "Employee":
            employee = frappe.get_doc("Employee", reminder.get("party"))
            if employee.company_email:
                recipients.append(employee.company_email)
        if recipients:
            frappe.sendmail(
                recipients=recipients,
                subject="Rental Reminder",
                message=f"This is a reminder for your upcoming rental: {reminder.get('name')} from {reminder.get('start_date')} to {reminder.get('end_date')}. Please ensure timely return of the equipment.",
                reference_doctype="Vehicle Rental",
                reference_name=reminder.get("name"),
                delayed=False)


# bench execute equipment_rental.tasks.get_rental_details --kwargs "{'equipment_name': '250820-000001'}"
@frappe.whitelist()
def get_rental_details(**kwargs):
    print(kwargs)
    equipment_name = kwargs.get("equipment_name")
    print(equipment_name)
    rental = frappe.get_doc("Equipment Master", equipment_name)
    # rental = frappe.get_doc("Equipment Rental", equipment_name)
    print(rental)
    return rental

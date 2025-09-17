import frappe

#bench execute equipment_rental.tasks.daily_task
@frappe.whitelist()
def daily_task():
    frappe.log("Running daily task")

#bench execute equipment_rental.tasks.rental_reminder --kwargs  "{'email':'test@test.com' ,'docname':'OFF-250421000012' }"
@frappe.whitelist()
def rental_reminder(**kwargs):
    print(kwargs.get("email"))
    frappe.log("Sending rental reminder emails")
    frappe.sendmail(
        recipients=["customer@example.com", kwargs.get("email")],
        subject="Rental Reminder",
        message="This is a reminder for your upcoming rental."
    )


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

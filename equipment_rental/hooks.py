app_name = "equipment_rental"
app_title = "Equipment Rental"
app_publisher = "John"
app_description = "EQ rent"
app_email = "yuntan0@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "equipment_rental",
# 		"logo": "/assets/equipment_rental/logo.png",
# 		"title": "Equipment Rental",
# 		"route": "/equipment_rental",
# 		"has_permission": "equipment_rental.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/equipment_rental/css/equipment_rental.css"
# app_include_js = "/assets/equipment_rental/js/equipment_rental.js"

# include js, css files in header of web template
# web_include_css = "/assets/equipment_rental/css/equipment_rental.css"
# web_include_js = "/assets/equipment_rental/js/equipment_rental.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "equipment_rental/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "equipment_rental/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "equipment_rental.utils.jinja_methods",
# 	"filters": "equipment_rental.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "equipment_rental.install.before_install"
# after_install = "equipment_rental.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "equipment_rental.uninstall.before_uninstall"
# after_uninstall = "equipment_rental.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "equipment_rental.utils.before_app_install"
# after_app_install = "equipment_rental.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "equipment_rental.utils.before_app_uninstall"
# after_app_uninstall = "equipment_rental.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "equipment_rental.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	# "all": [
	# 	"equipment_rental.tasks.all"
	# ],
	"daily": [
		"equipment_rental.tasks.daily_task"
	],
	# "hourly": [
	# 	"equipment_rental.tasks.hourly"
	# ],
	# "weekly": [
	# 	"equipment_rental.tasks.weekly"
	# ],
	# "monthly": [
	# 	"equipment_rental.tasks.monthly"
	# ],
    "cron": {
        # "0 0 * * *": [
        #     "equipment_rental.tasks.daily_task"
        # ],
        "0 9 * * *": [
            "equipment_rental.tasks.rental_reminder"
        ]
    }   
}

# Testing
# -------

# before_tests = "equipment_rental.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "equipment_rental.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "equipment_rental.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["equipment_rental.utils.before_request"]
# after_request = ["equipment_rental.utils.after_request"]

# Job Events
# ----------
# before_job = ["equipment_rental.utils.before_job"]
# after_job = ["equipment_rental.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"equipment_rental.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
    {"dt": "Client Script", "filters": [["module", "in", ["Equipment Rental"]]]},
    {"dt": "Print Format", "filters": [["module", "in", ["Equipment Rental"]]]},
    {"dt": "Server Script", "filters": [["module", "in", ["Equipment Rental"]]]},
    {
        "dt": "Report",
        "filters": [
            ["module", "in", ["Equipment Rental"]],
            ["report_type", "in", ["Script Report", "Query Report", "Custom Report"]],
        ],
    },
     {
        "dt": "Workflow",
        "filters": [
            [
                "name",
                "in",
                [
                    "Vehicle Rental Process",
                ],
            ]
        ],
    },
    {
        "dt": "Workflow State",
        "filters": [
            [
                "name",
                "in",
                [
                    "Reserved",
                    "On Rent",
                    "Extended",
                    "Draft",
                    "Cancelled",
                    "Return"
                ],
            ]
        ],
    },
    {
        "dt": "Workflow Action Master",
        "filters": [
            [
                "name",
                "in",
                [
                    "Extend",
                    "Request",
                    "Check in",
                    "Check out",
                    "Extend",
                    "Cancel"
                ],
            ]
        ],
    }
]
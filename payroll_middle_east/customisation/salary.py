import frappe
from datetime import datetime
from erpnext import get_region
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

# def update_salary(doc, method=None):
#     region = get_region(doc.company)
#     regions = ['UAE', 'Qatar', 'Saudi Arabia', 'Bahrain', 'Oman', 'Kuwait']
#     if region not in regions:
#         return
#     return 'Region found!'


# def create_custom_field_for_employee(doc, method=None):
#     region = get_region(doc.company)
#     regions = ['UAE', 'Qatar', 'Saudi Arabia', 'Bahrain', 'Oman', 'Kuwait']
#     if region not in regions:
#         return

#     pass


def make_employee_custom_fields():
    """Create Custom fields	
    - Employee name in Arabic
    """
    custom_fields = {

        'Employee': [
            dict(
                fieldname="employee_name_in_arabic",
                label="Name in Arabic",
                fieldtype="Data",
                insert_after="last_name",
            )
        ],

    }

    create_custom_fields(custom_fields, update=True)

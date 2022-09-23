from payroll_middle_east.customisation.salary import make_employee_custom_fields
import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field


def execute():
    # logger = frappe.logger("patch_log", allow_site=True, file_count=50)
    # logger.info(f"patches has started to execute")
    # regions = ['Saudi Arabia', 'UAE', 'Qatar', 'Oman', 'Kuwait', 'Bahrain']
    # companies = frappe.get_all('Company',
    #                            filters={'country':
    #                                     ['in', regions]
    #                                     },
    #                            pluck='company_name'
    #                            )
    # if not companies:
    #     logger.info('no companies found,returning')
    #     return
    # logger.info('companies found!')
    # employess = frappe.get_all(
    #     'Employee', filters={'company': ['in', companies]})

    # if not employess:
    #     logger.info('Employees not found,returning')
    #     return
    # logger.info('Making custom field for employee DocType')
    # make_employee_custom_fields()


    create_custom_field('Employee', {
        'fieldname': 'ewaybill',
        'label': 'E-Way Bill No.',
        'fieldtype': 'Data',        
        'allow_on_submit': 1,
        'insert_after': 'first_name',
        'translatable': 0,
        'owner': 'Administrator'
    })
from payroll_middle_east.customisation.salary import make_employee_custom_fields
import frappe



def execute():
    regions = ['Saudi Arabia', 'UAE', 'Qatar', 'Oman', 'Kuwait', 'Bahrain']
    companies = frappe.get_all('Company',
                               filters={'country':
                                        ['in', regions]
                                        },
                               pluck='company_name'
                               )
    if not companies:
        return

    employess = frappe.get_all(
        'Employee', filters={'company': ['in', companies]})

    if not employess:
        return

    make_employee_custom_fields()



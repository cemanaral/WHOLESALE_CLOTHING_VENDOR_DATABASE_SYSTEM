from flask_nav.elements import *
from flask_nav import Nav


topbar = Navbar('Wholesale Clothing Vendor Database System',
    View('Home', 'index'),
    Subgroup(
        'Employee',
        View('Show All Employees', 'read_employees'),
        View('Show top five earners', 'top_five_employees'),
        View('Show Departments of Employees', 'department_of_employees'),
        View('Create Employee', 'create_employee'),
        View('Delete Employee', 'delete_employee')
    ),
    Subgroup(
        'Department',
        View('Show Departments', 'read_department'),
        View('Show Managers', 'read_managers'),
        View('Average Age of Department', 'averageAgeOfDepartment'),
        View('Create Department', 'create_department'),
        View('Empty Manager', 'empty_manager'),
        View('Set Manager', 'set_manager'),
    ),
    Subgroup(
        'Clothing',
        View('Show Clothes', 'read_clothing'),
        View('Show Clothing Inventory Locations', 'read_clothing_inventory'),
        View('Show Clothing Types and Amounts', 'read_clothing_types'),
        View('Show Clothing Profits', 'read_clothing_profit'),
        View('Create Clothing', 'create_clothing'),
    ),
    Subgroup(

        'Producer',
        View('Show Producers', 'read_producer'),
        View('Create Producer', 'create_producer'),
    ),
    Subgroup(
        'Shop',
        View('Show Shops', 'read_shop'),

        'Shipment',
        View('Show Incoming Shipments', 'read_incoming_shipments'),
        View('Show Outgoing Shipments', 'read_outgoing_shipments'),
        View('Show Contracted Logistics Companies', 'read_name_of_logistics')

    ),
)    


nav = Nav()
nav.register_element('top', topbar)

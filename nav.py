from flask_nav.elements import *
from flask_nav import Nav


topbar = Navbar('Wholesale Clothing Vendor Database System',
    View('Home', 'index'),
    Subgroup(
        'Employee',
        View('Show All Employees', 'read_employees'),
        View('Show top five earners', 'top_five_employees'),
        View('Show Departments of Employees', 'department_of_employees'),
        View('Create Employee', 'create_employee')
    ),
)    


nav = Nav()
nav.register_element('top', topbar)

import flask_nav
from flask_nav.elements import Navbar, Separator, View, Text


topbar = Navbar('Wholesale Clothing Vendor Database System',
    View('Home', 'index'),
    View('Employee', 'read_employees'),
)

from flask_nav import Nav

nav = Nav()
nav.register_element('top', topbar)

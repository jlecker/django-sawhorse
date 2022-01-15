Django Sawhorse
===============

Sawhorse is an installable Django project intended to be used in the
development of "pluggable" Django apps. It eliminates the need to create an
"example project" which is used only in the development of the app.


Quick Start
-----------

1. Install and run where your package can can be imported. I recommend the
   parent directory of the package::
     
     pipenv install git+https://github.com/jlecker/django-sawhorse.git

2. That's it! You may now run Django management commands by using
   ``sawhorse-manage.py <app_name> <command>``, like so::
     
     sawhorse-manage.py my_app runserver
   
   If everything is working correctly, you should be able to run tests, run the
   development server, and run other commands to develop your app.
   

Additional Considerations
-------------------------

If your app has settings which are required to run out-of-the-box, they can be
placed in the module *required_settings.py*. This can be placed anywhere it can
be imported, but the recommended location is wherever you are running Sawhorse.

The *required_settings.py* module can be kept with your app so that it can be
easily developed with Sawhorse, but if your app also requires API keys or other
"secret" settings, they can be placed in the module *local_settings.py* in
the same directory. Presumably you would NOT keep this file with the app, so
make sure any such settings requirements are well-documented elsewhere.

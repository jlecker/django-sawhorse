Django Sawhorse
===============

Sawhorse is an installable Django project intended to be used in the
development of "standalone" Django apps. It is designed to eliminate the need
to create an "example project" which is used only in the development of the
app. It is the "example project" for any app.


Quick Start
-----------

1. Add ``export SAWHORSE_HOME=$HOME/projects`` to your shell startup file
   (modify the path to your desired location). Sawhorse will create a
   subdirectory in this location for every app that you use with it. This is
   similar to the way ``WORKON_HOME`` works in virtualenvwrapper (which you
   should be using anyway, especially since Sawhorse requires it).

2. Use pip to install Sawhorse into the development virtualenv for an app. For
   now, the best way to do this is to install directly from GitHub::
     
     pip install git+https://github.com/jlecker/django-sawhorse.git

3. That's it! You may now run Django management commands by using
   ``sawhorse-manage.py``, like so::
     
     sawhorse-manage.py runserver


Additional Considerations
-------------------------

If your app has settings which are required to run out-of-the-box, they can be
placed in the module *required_settings.py*. The recommended location for this
module is in the root directory of your app (NOT the package directory, but
where you keep things like the README, setup.py, etc). This is also where you
should run sawhorse-manage.py.

The *required_settings.py* module can be kept with your app so that it can be
easily run with Sawhorse, but if your app also requires API keys or other
"secret" settings, they can be placed in the module *local_settings.py* in
the same directory. Presumably you would NOT keep this file with the app, so
make sure any such settings requirements are well-documented elsewhere.

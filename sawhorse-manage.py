#!/usr/bin/env python

import os, sys

if __name__ == '__main__':
    
    sawhorse_home = os.environ.get('SAWHORSE_HOME')
    if not sawhorse_home:
        raise Exception('Required environment variable SAWHORSE_HOME not found.')
    if not os.path.exists(sawhorse_home):
        raise Exception('Path specified in SAWHORSE_HOME does not exist. Aborting.')
    
    workon_home = os.environ.get('WORKON_HOME')
    if not workon_home:
        raise Exception('WORKON_HOME not found in environment. Sawhorse requires virtualenvwrapper.')
    
    venv = os.environ.get('VIRTUAL_ENV')
    if not venv:
        raise Exception('No virtualenv activated.')

    if venv.find(workon_home):
        raise Exception('Active virtualenv not in WORKON_HOME. Aborting.')

    # if SAWHORSE_APP is not set, attempt to guess from virtualenv name
    app_name = os.environ.setdefault('SAWHORSE_APP', venv[len(workon_home) + 1:])
    app_root = os.path.join(sawhorse_home, app_name)
    if not os.path.exists(app_root):
        os.mkdir(app_root, 0755)
    
    os.environ['DJANGO_SETTINGS_MODULE'] = 'sawhorse.settings'

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

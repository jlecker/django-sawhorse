#!/usr/bin/env python

import os, sys

if __name__ == '__main__':
    
    if not os.environ.get('SAWHORSE_HOME'):
        raise Exception('Required environment variable SAWHORSE_HOME not found.')
    
    wh = os.environ.get('WORKON_HOME')
    if not wh:
        raise Exception('WORKON_HOME not found in environment. Sawhorse requires virtualenvwrapper.')
    
    ve = os.environ.get('VIRTUAL_ENV')
    if not ve:
        raise Exception('No virtualenv activated.')

    if ve.find(wh):
        raise Exception('Active virtualenv not in WORKON_HOME. Aborting.')

    # if SAWHORSE_APP is not set, attempt to guess from virtualenv name
    os.environ.setdefault('SAWHORSE_APP', ve[len(wh) + 1:])
    
    os.environ['DJANGO_SETTINGS_MODULE'] = 'sawhorse.settings'

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

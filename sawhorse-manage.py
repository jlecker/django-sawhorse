#!/usr/bin/env python

import os, sys

if __name__ == '__main__':

    app_name = sys.argv[1]
    
    cwd = os.getcwd()
    sys.path.append(cwd)

    sawhorse_root = os.path.join(cwd, '_sawhorse')
    if not os.path.exists(sawhorse_root):
        os.mkdir(sawhorse_root, 0o755)

    os.environ['SAWHORSE_APP'] = app_name
    os.environ['SAWHORSE_ROOT'] = sawhorse_root

    os.environ['DJANGO_SETTINGS_MODULE'] = 'sawhorse.settings'


    from django.core.management import execute_from_command_line

    args = sys.argv[:]
    args.pop(1)
    execute_from_command_line(args)

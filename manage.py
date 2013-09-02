#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tasker.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
>>>>>>> 25b6aa8f3bbdef582677c44362785359baceeb94

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

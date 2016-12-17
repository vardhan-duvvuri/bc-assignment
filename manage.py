#!/usr/bin/env python
import os
import sys

# Since Python 3.4/ Django 1.9 is currently not supporting
# MySQLdb package, we installed pymysql package and guiding
# django to use pymysql as MySQLdb package

try:
    """
        Importing pymysql package instead of using
        MySQLdb
    """
    import pymysql
    pymysql.install_as_MySQLdb()
except:
    pass

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beautycode.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

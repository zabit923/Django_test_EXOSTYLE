import os

import django
from django.core.management import execute_from_command_line

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.settings")
django.setup()

execute_from_command_line(["manage.py", "dumpdata", "products.ProductCategory", "--indent", "2",
                           "--output", "categories.json"])
execute_from_command_line(["manage.py", "dumpdata", "products.Product", "--indent", "2", "--output", "goods.json "])

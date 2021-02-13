from django.db import migrations

from www.populate_db import populate_db, depopulate_db


class Migration(migrations.Migration):
    dependencies = [
        ("www", "0001_initial"),
    ]

    operations = [migrations.RunPython(populate_db, reverse_code=depopulate_db)]

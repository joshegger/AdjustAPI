from __future__ import unicode_literals
import os, csv, sys, django
from django.conf import settings
from django.db import migrations

ROOT_PROJECT_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
sys.path.append(ROOT_PROJECT_PATH)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'adjust.settings')
django.setup()


def init_db(apps, schema_editor):
    Metrics = apps.get_model('api', 'Metrics')
    with open(os.path.join(settings.BASE_DIR, 'dataset.csv')) as csvfile:
        for row in csv.DictReader(csvfile):
            Metrics.objects.create(**row)


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init_db, migrations.RunPython.noop),
    ] if not settings.TESTING else []

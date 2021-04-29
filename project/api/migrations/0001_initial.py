

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metrics',
            fields=[
                ('created_at', models.DateField(auto_created=True, blank=True, default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('channel', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('os', models.CharField(blank=True, max_length=100, null=True)),
                ('impressions', models.IntegerField(blank=True, null=True)),
                ('clicks', models.IntegerField(blank=True, null=True)),
                ('installs', models.IntegerField(blank=True, null=True)),
                ('spend', models.FloatField(blank=True, null=True)),
                ('revenue', models.FloatField(blank=True, null=True)),
                ('CPI', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Metrics',
            },
        ),
    ]

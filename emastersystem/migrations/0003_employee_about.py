# Generated by Django 4.1 on 2022-08-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emastersystem', '0002_remove_employee_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='about',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]

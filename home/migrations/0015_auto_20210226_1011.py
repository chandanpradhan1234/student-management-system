# Generated by Django 3.1.6 on 2021-02-26 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20210226_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateTimeField(null=True),
        ),
    ]
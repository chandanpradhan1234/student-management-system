# Generated by Django 3.1.6 on 2021-02-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
# Generated by Django 2.1.2 on 2019-06-22 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20190622_1612'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('student', 'date')},
        ),
    ]

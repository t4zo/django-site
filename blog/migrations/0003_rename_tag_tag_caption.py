# Generated by Django 3.2.3 on 2021-05-25 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210525_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='caption',
        ),
    ]

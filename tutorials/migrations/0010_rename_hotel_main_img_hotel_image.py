# Generated by Django 4.0.5 on 2022-06-13 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0009_hotel_delete_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_Main_Img',
            new_name='image',
        ),
    ]

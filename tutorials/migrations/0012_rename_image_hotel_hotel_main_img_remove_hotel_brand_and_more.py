# Generated by Django 4.0.5 on 2022-06-13 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0011_hotel_brand_hotel_coordinate1_hotel_coordinate2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='image',
            new_name='hotel_Main_Img',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='coordinate1',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='coordinate2',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='referenceobjectsize',
        ),
    ]

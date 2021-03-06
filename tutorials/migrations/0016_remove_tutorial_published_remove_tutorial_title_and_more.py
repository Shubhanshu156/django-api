# Generated by Django 4.0.5 on 2022-06-14 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0015_hotel_is_verify_hotel_ref_object_size_height_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='published',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='title',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='brand',
            field=models.CharField(default='shree cement', max_length=200),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='coordinate1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='coordinate2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='is_verify',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='object_size_height',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='object_size_width',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='ref_object_size_height',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='ref_object_size_width',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

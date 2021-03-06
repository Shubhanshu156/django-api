# Generated by Django 4.0.5 on 2022-06-14 07:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0019_remove_register_createtime_remove_register_lasttime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='createtime',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='lasttime',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='createddate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='lastdate',
            field=models.DateField(auto_now=True),
        ),
    ]

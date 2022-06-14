# Generated by Django 4.0.5 on 2022-06-14 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0018_register_createtime_register_lasttime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='createtime',
        ),
        migrations.RemoveField(
            model_name='register',
            name='lasttime',
        ),
        migrations.AddField(
            model_name='register',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='register',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='register',
            name='createddate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='lastdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

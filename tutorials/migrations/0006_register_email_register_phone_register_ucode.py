# Generated by Django 4.0.5 on 2022-06-13 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0005_remove_register_email_remove_register_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='email',
            field=models.CharField(default='shubhanshusharma2712@gmail.com', max_length=50),
        ),
        migrations.AddField(
            model_name='register',
            name='phone',
            field=models.CharField(default='1234567890', max_length=10),
        ),
        migrations.AddField(
            model_name='register',
            name='ucode',
            field=models.CharField(default='0', max_length=10),
        ),
    ]

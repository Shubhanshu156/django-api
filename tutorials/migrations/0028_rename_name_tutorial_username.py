# Generated by Django 4.0.5 on 2022-06-14 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0027_rename_name_upload_username_alter_register_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='name',
            new_name='username',
        ),
    ]

# Generated by Django 4.0.2 on 2022-02-21 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_useraccount_options_useraccount_area_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='profile_picture',
            field=models.FileField(default='', upload_to=''),
        ),
    ]

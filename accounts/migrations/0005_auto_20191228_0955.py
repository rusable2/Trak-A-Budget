# Generated by Django 3.0 on 2019-12-28 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191228_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ind_user',
            name='document',
            field=models.FileField(blank=True, default='Ind_User_Data.xlsx', null=True, upload_to='documents/'),
        ),
    ]

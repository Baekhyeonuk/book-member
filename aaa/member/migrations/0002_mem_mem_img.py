# Generated by Django 3.2.6 on 2021-08-17 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mem',
            name='Mem_img',
            field=models.FileField(blank='True', default='', null=True, upload_to='member/%Y-%m-%d', verbose_name='사진'),
        ),
    ]

# Generated by Django 4.0 on 2022-05-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apifruit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='Image',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]

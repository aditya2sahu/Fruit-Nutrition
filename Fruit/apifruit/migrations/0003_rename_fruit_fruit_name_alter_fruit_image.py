# Generated by Django 4.0 on 2022-05-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apifruit', '0002_alter_fruit_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fruit',
            old_name='Fruit',
            new_name='Name',
        ),
        migrations.AlterField(
            model_name='fruit',
            name='Image',
            field=models.ImageField(default=' ', upload_to='image'),
        ),
    ]
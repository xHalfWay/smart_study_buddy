# Generated by Django 4.2.11 on 2024-04-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_buddy', '0010_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pair',
            name='first_element_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='pair',
            name='second_element_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]

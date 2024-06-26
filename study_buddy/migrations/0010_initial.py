# Generated by Django 4.2.11 on 2024-04-26 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('study_buddy', '0009_remove_pair_task_delete_findpairtask_delete_pair'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_element_text', models.CharField(blank=True, max_length=100, null=True)),
                ('first_element_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('second_element_text', models.CharField(blank=True, max_length=100, null=True)),
                ('second_element_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_buddy.task')),
            ],
        ),
    ]

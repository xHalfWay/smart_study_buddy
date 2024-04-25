# Generated by Django 4.2.11 on 2024-04-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('study_buddy', '0004_remove_userprofile_role_remove_userprofile_roles_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='tasks/')),
                ('file', models.FileField(blank=True, null=True, upload_to='tasks/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 4.2.11 on 2024-04-24 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study_buddy', '0002_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_profile', to='study_buddy.role'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='roles',
            field=models.ManyToManyField(related_name='user_profiles', to='study_buddy.role'),
        ),
    ]
# Generated by Django 5.1.4 on 2024-12-11 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_user_is_agent_user_is_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.agent'),
        ),
    ]
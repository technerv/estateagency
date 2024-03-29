# Generated by Django 3.2.9 on 2021-12-12 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('estateapp', '0003_auto_20211210_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agentuser', to='accounts.user'),
        ),
        migrations.AlterField(
            model_name='property',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent', to='accounts.user'),
        ),
    ]

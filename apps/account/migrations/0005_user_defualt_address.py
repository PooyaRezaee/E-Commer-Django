# Generated by Django 4.1.3 on 2022-12-06 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_address_to'),
        ('account', '0004_alter_otpcode_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='defualt_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.address'),
        ),
    ]
# Generated by Django 4.1.3 on 2023-09-28 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudstart', '0002_alter_user_email_alter_user_name_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
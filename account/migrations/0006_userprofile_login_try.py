# Generated by Django 4.2.5 on 2023-09-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_uploadbooks_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='login_try',
            field=models.IntegerField(default=3),
        ),
    ]

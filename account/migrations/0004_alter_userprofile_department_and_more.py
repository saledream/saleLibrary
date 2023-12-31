# Generated by Django 4.2.5 on 2023-09-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_userprofile_downloaded_books_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='department',
            field=models.CharField(choices=[('', ''), ('computer science', 'computer science'), ('marketing', 'marketing'), ('accounting and finance', 'accounting and finance')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='ProfilePhoto/%Y/%m/%d'),
        ),
    ]

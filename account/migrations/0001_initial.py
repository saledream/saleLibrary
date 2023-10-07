# Generated by Django 4.2.5 on 2023-09-25 00:19

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookstore', '0006_bookinfo_slug_bookinfo_upload_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, default='../static/male_avator.png', upload_to=account.models.set_profile_photo)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('bio', models.CharField(blank=True, max_length=50, null=True)),
                ('downloaded_books', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='download_books', to='bookstore.bookinfo')),
                ('upload_books', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='upload_books', to='bookstore.bookinfo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

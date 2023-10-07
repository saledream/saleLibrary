# Generated by Django 3.2.19 on 2023-09-20 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=700, null=True)),
                ('price', models.IntegerField(null=True)),
                ('edition', models.CharField(max_length=150, null=True)),
                ('publisher', models.CharField(max_length=150, null=True)),
                ('cover', models.ImageField(upload_to='booksCover/')),
            ],
        ),
    ]
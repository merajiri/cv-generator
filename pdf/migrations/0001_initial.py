# Generated by Django 4.1.5 on 2023-01-25 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField()),
                ('degree', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
                ('univercity', models.CharField(max_length=200)),
                ('skills', models.TextField()),
                ('previous_works', models.TextField()),
            ],
        ),
    ]

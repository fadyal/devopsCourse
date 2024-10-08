# Generated by Django 5.1.1 on 2024-09-25 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('director', models.CharField(max_length=100)),
                ('main_actors', models.CharField(max_length=200)),
                ('year_of_release', models.IntegerField()),
                ('poster', models.ImageField(upload_to='posters/')),
            ],
        ),
    ]

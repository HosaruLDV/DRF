# Generated by Django 4.1.7 on 2023-03-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lern', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.CharField(max_length=250, verbose_name='превью'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.CharField(max_length=250, verbose_name='превью'),
        ),
    ]

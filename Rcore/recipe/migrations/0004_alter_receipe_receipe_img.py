# Generated by Django 4.2.15 on 2024-10-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_receipe_delete_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='receipe_img',
            field=models.ImageField(upload_to='receipe'),
        ),
    ]

# Generated by Django 3.2 on 2021-04-18 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]

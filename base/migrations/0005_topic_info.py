# Generated by Django 4.2.7 on 2024-02-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_post_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='info',
            field=models.CharField(max_length=500, null=True),
        ),
    ]

# Generated by Django 5.0.3 on 2024-05-01 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_remove_tag_user_utilizador_user_alter_review_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='data',
            field=models.DateField(default=datetime.datetime(2024, 5, 1, 18, 9, 54, 769371, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='utilizador',
            name='profileImage',
            field=models.ImageField(default='ProjetoDIAM\x08ackend\\website\\static\\images\no-profile-img.png', upload_to=''),
        ),
    ]

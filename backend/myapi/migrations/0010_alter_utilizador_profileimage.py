# Generated by Django 5.0.4 on 2024-05-12 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0009_remove_review_mainimage_remove_review_reviewid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilizador',
            name='profileImage',
            field=models.ImageField(default='/images/no-profile-img.png', upload_to=''),
        ),
    ]

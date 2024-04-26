# Generated by Django 5.0.4 on 2024-04-15 02:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Explorer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('profileImage', models.ImageField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('description', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=200)),
                ('mainImage', models.ImageField(default='', upload_to='')),
                ('favoritePlaces', models.ManyToManyField(related_name='favoritePlaces', to='myapi.explorer')),
                ('userID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapi.explorer')),
                ('tags', models.ManyToManyField(related_name='places', to='myapi.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('mainImage', models.ImageField(default='', upload_to='')),
                ('numLikes', models.IntegerField(default=0)),
                ('numDisLikes', models.IntegerField(default=0)),
                ('placeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.place')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.explorer')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
                ('numLikes', models.IntegerField(default=0)),
                ('numDisLikes', models.IntegerField(default=0)),
                ('postID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.post')),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, null=True)),
                ('like', models.BooleanField(null=True)),
                ('commentID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.comment')),
                ('placeID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.place')),
                ('postID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.post')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.explorer')),
            ],
        ),
    ]
# Generated by Django 5.0.4 on 2024-04-26 09:10

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reaction',
            name='commentID',
        ),
        migrations.RemoveField(
            model_name='post',
            name='placeID',
        ),
        migrations.RemoveField(
            model_name='post',
            name='userID',
        ),
        migrations.RemoveField(
            model_name='reaction',
            name='postID',
        ),
        migrations.RemoveField(
            model_name='reaction',
            name='placeID',
        ),
        migrations.RemoveField(
            model_name='reaction',
            name='userID',
        ),
        migrations.RemoveField(
            model_name='place',
            name='tags',
        ),
        migrations.AddField(
            model_name='place',
            name='reviewNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='place',
            name='rating',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.RenameModel(
            old_name='Explorer',
            new_name='Utilizador',
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300, null=True)),
                ('rating', models.SmallIntegerField(null=True)),
                ('mainImage', models.ImageField(default='', upload_to='')),
                ('data', models.DateField(default=datetime.datetime(2024, 4, 26, 9, 10, 3, 317751, tzinfo=datetime.timezone.utc))),
                ('likedTags', models.ManyToManyField(related_name='likedTags', to='myapi.tag')),
                ('placeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.place')),
                ('reviewID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.review')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.utilizador')),
            ],
        ),
        migrations.CreateModel(
            name='TagPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeNumber', models.IntegerField(default=1)),
                ('placeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.place')),
                ('tagID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.tag')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Reaction',
        ),
    ]
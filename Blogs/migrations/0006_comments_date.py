# Generated by Django 2.2 on 2021-04-09 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0005_blog_coments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

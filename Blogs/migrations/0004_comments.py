# Generated by Django 2.2 on 2021-04-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0003_blog_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.TextField()),
            ],
        ),
    ]
# Generated by Django 2.2.7 on 2020-04-09 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('posts', models.ManyToManyField(blank=True, to='posts.Post')),
            ],
        ),
    ]

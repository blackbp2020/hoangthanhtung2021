# Generated by Django 3.1 on 2020-09-24 17:01

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=35)),
                ('slug', models.CharField(max_length=250)),
                ('Created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='tintuc',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('TenBai', models.CharField(max_length=500)),
                ('noidung', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]

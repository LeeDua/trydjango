# Generated by Django 2.2.8 on 2019-12-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgUpload', '0002_auto_20191211_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='imgupload',
            name='name',
            field=models.TextField(default='someimg'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0.6 on 2019-10-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikimodel',
            name='entryInfo',
            field=models.CharField(max_length=10000),
        ),
    ]

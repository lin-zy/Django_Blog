# Generated by Django 2.1.1 on 2018-12-16 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='modified_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

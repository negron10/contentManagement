# Generated by Django 2.2.7 on 2019-12-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='createDates',
            field=models.DateField(default='2019-10-12'),
        ),
        migrations.AlterField(
            model_name='content',
            name='createDates',
            field=models.DateField(default='2019-10-12'),
        ),
    ]

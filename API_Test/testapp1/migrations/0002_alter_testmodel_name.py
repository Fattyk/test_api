# Generated by Django 3.2.9 on 2021-11-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='name',
            field=models.CharField(default='Null', max_length=225, unique=True),
        ),
    ]

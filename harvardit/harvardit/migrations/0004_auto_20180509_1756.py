# Generated by Django 2.0.4 on 2018-05-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvardit', '0003_auto_20180509_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='students',
            field=models.ManyToManyField(blank=True, to='harvardit.Student'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-10-02 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskinput',
            name='dayToGo',
            field=models.IntegerField(default=0),
        ),
    ]

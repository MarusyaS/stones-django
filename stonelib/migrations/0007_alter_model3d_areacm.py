# Generated by Django 3.2.15 on 2023-06-09 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stonelib', '0006_auto_20230609_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model3d',
            name='AreaCM',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
# Generated by Django 4.2.6 on 2023-10-31 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_disease', '0002_heartdiseaseprediction_prediction_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heartdiseaseprediction',
            name='prediction_results',
            field=models.IntegerField(null=True),
        ),
    ]

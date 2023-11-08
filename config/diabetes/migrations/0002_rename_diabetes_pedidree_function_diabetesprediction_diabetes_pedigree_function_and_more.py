# Generated by Django 4.2.6 on 2023-11-08 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diabetesprediction',
            old_name='diabetes_Pedidree_Function',
            new_name='diabetes_Pedigree_Function',
        ),
        migrations.AddField(
            model_name='diabetesprediction',
            name='skin_Tickness',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

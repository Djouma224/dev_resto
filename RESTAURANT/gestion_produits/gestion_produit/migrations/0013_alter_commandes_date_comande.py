# Generated by Django 5.0.3 on 2024-04-23 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_produit', '0012_remove_commande_date_comande_commandes_date_comande'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commandes',
            name='date_comande',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

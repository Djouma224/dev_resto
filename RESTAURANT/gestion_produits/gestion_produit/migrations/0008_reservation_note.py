# Generated by Django 4.1.1 on 2024-04-01 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_produit', '0007_remove_reservation_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]

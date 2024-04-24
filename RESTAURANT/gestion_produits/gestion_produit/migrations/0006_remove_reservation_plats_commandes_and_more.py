# Generated by Django 4.1.1 on 2024-04-01 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion_produit', '0005_remove_reservation_num_table_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='plats_commandes',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='reservation',
        ),
        migrations.AddField(
            model_name='reservation',
            name='client',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='phone_number',
            field=models.CharField(default=0, max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='statu',
            field=models.CharField(choices=[('confirmée', 'confirmée'), ('en attente', 'en attente'), ('annulée', 'annulée')], default='en attente', max_length=32),
        ),
    ]

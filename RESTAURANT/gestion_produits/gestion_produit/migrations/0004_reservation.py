# Generated by Django 5.0.1 on 2024-02-13 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_produit', '0003_alter_commentaires_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num_table', models.CharField(max_length=5)),
                ('date', models.DateField()),
                ('heure', models.TimeField()),
                ('nombre_personnes', models.IntegerField()),
                ('plats_commandes', models.ManyToManyField(to='gestion_produit.produits')),
            ],
        ),
    ]

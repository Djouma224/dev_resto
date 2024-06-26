# Generated by Django 5.0.3 on 2024-04-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_produit', '0013_alter_commandes_date_comande'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCommande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=50)),
                ('tel_livraison', models.CharField(max_length=12)),
                ('livraison', models.CharField(max_length=50)),
                ('date_comande', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='commandes',
            name='date_comande',
        ),
        migrations.AddField(
            model_name='commandes',
            name='coordonnes',
            field=models.ManyToManyField(to='gestion_produit.usercommande'),
        ),
    ]

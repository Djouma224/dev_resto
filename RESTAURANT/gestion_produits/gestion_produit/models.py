from django.db import models
# from django.contrib import admin
from django.urls import reverse
from gestion_compte.models import utilisateurs
# il faut importer cette variable que nous avons créer dans settings qui pointer notre model utilisateur personnaliser
from gestion_produits.settings import AUTH_USER_MODEL
# Create your models here.

class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=50)

    class Meta:
        verbose_name=("Categorie")
        verbose_name_plural=("Categories")
        
    def __str__(self):
        return self.nom_categorie


class Produits(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    prix = models.PositiveIntegerField()
    image = models.ImageField(upload_to='%Y/%m/%d',blank=True,null=True)
    date = models.DateField(auto_now=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    # fn pour afficher un btn lien dans l'admin vers detail
    # def get_absolute_url(self):
    #     return reverse("detail_produit", kwargs={"my_id": self.my_id})

    class Meta:
        verbose_name=("Produits")
        verbose_name_plural=("Produits")

    def __str__(self):
        return self.nom
     
# La gestion du panier de l'utilisateur:
# pour cela on a besoin de 2 models suplementaires 1er representer les arcticle que l'utilisateur souhaite acheter
# un 2em represente le panier de l'utilisateur qui sera lier a ces articles
# NB: Article(Order),  # Panier(Card)
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Produits, on_delete=models.CASCADE)
    qte = models.IntegerField(default=1)
    commander = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.nom} ({self.qte})"
    
class Card(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    date_comande = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    
class Commentaires(models.Model):
    message = models.TextField(null=True)
    date = models.DateField(auto_now_add=True)
    userP = models.ForeignKey(utilisateurs,on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Commentaire')
        verbose_name_plural = ('commenamentaire')

    def __str__(self):
        return f'{self.message}'



# Model pour la gestion des reservations
class Reservation(models.Model):
   # Num_table = models.CharField(max_length=5)
    type_reservation = [
       ("Ceremonie Mariage","Ceremonie Mariage"),
       ("Aniversaire","Aniversaire"),
       ("Dîner","Dîner")
        ]
    status = [
        ("confirmée","confirmée"),
        ("en attente","en attente"),
        ("annulée","annulée")
    ]
    client = models.ForeignKey(utilisateurs,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length = 9)
    date = models.DateField()
    heure = models.TimeField()
    reservation = models.CharField(max_length = 32, choices =type_reservation, default = "Dîner")
    statu = models.CharField(max_length = 32,choices = status, default = "en attente")
    #nombre_personnes = models.IntegerField()
    note = models.TextField(blank = True)
    #plats_commandes = models.ManyToManyField(Produits)
    

    def __str__(self):
        return f"Réservation du {self.date} à {self.heure} pour {self.reservation}"
from django.urls import reverse
from .models import Categorie, Commentaires, Produits
# def cart(request):
# #     #recuperer le panier de l'utilisateur. la fn ci_dessous renvoi l'objet s'il exite ou renvoie une erreur sinon
#     cart = Card(user = request.user)
#     nb = cart.orders.count()
#     orders = cart.orders.all()
#     context={'nb':nb,'orders':orders}# tout les elements de notre panier
#     return context


def commentaire(request):
    
    if request.method == 'POST':
        msg = request.POST.get('message')
        com = Commentaires.objects.create(
            message=msg,
            userP=request.user)
        com.save()
    comment = Commentaires.objects.all()
    context = {'comment':comment}
    return context


def list_menu(request):
    donnees = Produits.objects.all()
    cat = Categorie.objects.all()
    context = {'donnees':donnees,"cat":cat}
    return context

# def aff_categories(request,id_categorie):
#     cat = Categorie.objects.all()
#     categorie = Categorie.objects.get(id=id_categorie)
#     produit = Produits.objects.filter(categorie=categorie)
#     context = {"categorie":categorie,         
#                "produit":produit,
#                "cat":cat}
#     return context


#from django.http import JsonResponse
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
<<<<<<< HEAD
from .models import Produits,Categorie,Card,Order,Commentaires,Commande,Commandes,UserCommande
=======
from .models import Produits,Categorie,Card,Order,Commentaires, Reservation
>>>>>>> origin/master
from django.urls import reverse 
from django.contrib.auth.decorators import login_required


# Fontion pour afficher tout les produits
def list_menu(request):
    # donnees = Produits.objects.all()
    # cat = Categorie.objects.all()
    # context = {'donnees':donnees}
   
    return render(request, 'gestion_produit/index_2.html')


# Fontion pour afficher les details d'un produit
def detail_produit(request,my_id):
    var = get_object_or_404(Produits,pk=my_id)
    contexte = {'var':var}
    return render(request,'gestion_produit/single-product.html',contexte)

# fonction permettant d'afficher tout les produits dans all_products.html
def all_products(request):
    donnees = Produits.objects.all()
    context = {'donnees':donnees}
    return render(request, 'gestion_produit/all.html',context)


# afficher les produits rechercher dans recherche.html
def recherche(request):
    if request.method == 'GET':
        var = request.GET.get("search")
        produit =Produits.objects.filter(nom__icontains=var)|Produits.objects.filter(categorie__nom_categorie__icontains=var)
        context = {'produit':produit}
    return render(request,'gestion_produit/recherche.html',context)

# fn pour afficher les categories
def aff_categories(request,id_categorie):
    categorie = Categorie.objects.get(id=id_categorie)
    produit = Produits.objects.filter(categorie=categorie)
    context = {"categorie":categorie,         
               "produit":produit}
    return render(request, 'gestion_produit/categories.html',context)

def contact(request):
    
    return render(request,'gestion_produit/contact.html')

def apropos(request):
    
    return render(request,'gestion_produit/about.html')

def reservation(request):
    
    type_reservation = Reservation.type_reservation
    
    
    
    
    if request.method == 'POST':
        
        user = request.user
        type_reserve = request.POST.get('reservation')
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        tel = request.POST.get('tel')
        message = request.POST.get('message')
        
        
        date = datetime.strptime(date_str, '%Y-%m-%d').date()  # Convertir en objet datetime.date
        time = datetime.strptime(time_str, '%H:%M').time()  # Convertir en objet datetime.time
        
        
        existing_reservation = Reservation.objects.filter( date=date, heure =time, reservation = "Ceremonie Mariage")
        
        if existing_reservation.exists():
            # Si le créneau est pris, vous pouvez afficher un message d'erreur ou rediriger vers une autre page
           messages.error(request, 'Ce créneau est déjà pris. Veuillez choisir un autre.')
        
        # Vérifier si le créneau est dans le passé
        
        elif (timezone.make_aware(timezone.datetime.combine(date, time)) < timezone.now()):
            # Si le créneau est dans le passé, affichez un message d'erreur
           messages.error(request, 'Vous ne pouvez pas réserver dans le passé.')
        
        # Créer le rendez-vous
          # Redirige vers la page de confirmation du rendez-vous
    
        else:
            reservation = Reservation.objects.create(client=user, phone_number=tel, date=date, heure=time, reservation = type_reserve, note = message)
            reservation.save()
        
            return redirect('list_menu')
    error_messages = messages.get_messages(request)
    
    context = {
        "type_reservation": type_reservation,
        "error_messages":error_messages
    }

    return render(request,'gestion_produit/reservation.html',context)



    # fonction pour les commentaires
@login_required(login_url='/login')
def commentaire(request):
    
    # if request.method == 'POST':
    #     msg = request.POST.get('message')
    #     user = request.user
    #     if user:
    #         com = Commentaires.objects.create(
    #         message=msg,
    #         userP=user)
    #     com.save()
    #     return reverse('list_menu')
    pass
    

#voit les commentaire
def view_comment(request):
    comment = Commentaires.objects.all()
    return render(request,'gestion_produit/voir_comment.html',comment)

@login_required(login_url='/login')
def add_to_card(request,my_id):
    # recuperer notre utilisateur
    user =request.user
    # recuperer le produit
    product = get_object_or_404(Produits,id=my_id)
    # recuperer le panier de l'utilisateur s'il exite ou le créer sinon
    #elle a besoin de 2 variable la methode retourne 2 elements elle va returner dans "cart" l'objet en question qu'il a été créer ou qu'il exite déjà et
    #retourne dans une 2em variable une information pournon savoir si l'objet à été créer ou non elle va nous servir si l'objet est déja ajouté dans le panier de l'incrémenté
    #par convention on met (_) signifie que la la 2em variable ne sera pas utiliser  
    cart, _ = Card.objects.get_or_create(user=user)
    # recuperer l'élement qui va être dans notre panier  
    order, crated = Order.objects.get_or_create(user=user,
                                                product=product)
    # si l'objet est créer. c'st le cas ou si l'element n'exitait pas dans le panier donc il faut l'ajouter
    if crated:
        cart.orders.add(order)
        cart.save()# sauvegarder le panier
    else:
        order.qte += 1
        order.save()
    return redirect(reverse("list_menu"))


# fn qui affiche le panier de l'utilisateur
def cart(request):
    user=request.user
   # recuperer le panier de l'utilisateur. la fn ci_dessous renvoi l'objet s'il exite ou renvoie une erreur sinon
    cart,created = Card.objects.get_or_create(user=request.user)
    orders = cart.orders.all()
    nb = cart.orders.count()
    total_price = cart.calculate_total_price()

    if nb !=0:
        if request.method == 'POST':
            tel_livraison = request.POST.get('tel_livraison')
            adresse = request.POST.get('adresse')
            livraison = request.POST.get('livraison')
            print(tel_livraison)
            
            user_commande=UserCommande.objects.create(adress=adresse,
                                            tel_livraison=tel_livraison,
                                            livraison=livraison)
                                            
            user_commande.save()
            # user=request.user
            card = Card.objects.get(user=user)
            # orders = card.orders.all()
            orders = Order.objects.filter(user=user)
            
            produits = Commandes.objects.create(user=user.username)
            # produits.coordonnes.add(user_commande)

            for order in orders:
                new=Commande.objects.create(
                                        nom=order.product.nom,
                                        qte=order.qte )
                produits.produits.add(new)

                new.save()
                order.delete()

            card.delete()
            return render(request, 'gestion_produit/cart.html')
        else:
            print("Votre panier est vide pour le moment !!!")
    
    context={"orders":orders,
             'nb':nb,
             'total_price':total_price
             }# tout les elements de notre panier
    return render(request, 'gestion_produit/cart.html',context)

#fn pour mise a jour des quantites:
def update_qte(request,order_id):
    order=Order.objects.get(id=order_id)
    order.ajout_qte()
    return redirect('cart')

def dimininuer_qte(request,order_id):
    order=Order.objects.get(id=order_id)
    order.dimininuer_qte()
    return redirect('cart')

# fn pour supprimer un produit dans le panier
def del_prod_card(request,my_id):
    product_del = get_object_or_404(Order,id=my_id)
    product_del.delete()
    return redirect('cart')
# fn commander 
def commander(request):
    user=request.user
    card = Card.objects.get(user=user)
    # orders = card.orders.all()
    orders = Order.objects.filter(user=user)
    print(user.username)
    
        # produits = Commandes.objects.create(user=user.username)
        
        # for order in orders:
        #     new=Commande.objects.create(
        #                                 nom=order.product.nom,
        #                                     qte=order.qte )
        #     produits.produits.add(new)

        #     new.save()
        #     order.delete()
        #     produits.coordonnes.add(user_commande)
   
        # card.delete()
    return render(request,'gestion_produit/cart.html',{'card':card,'orders':orders})
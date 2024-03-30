from django.urls import path
from gestion_produit.views import list_menu,all_products,detail_produit,recherche,contact,apropos,add_to_card,cart,del_prod_card,aff_categories,reservation
urlpatterns = [
    # url pour affihcer les details d'un produit
    path('detail_produit/<int:my_id>/',detail_produit,name='detail_produit'),
    # url pour ajouter un prodduit au panier
    path('detail_produit/add_to_card/<int:my_id>',add_to_card,name='add_to_card'),

    # url pour supprimer un produit dans le panier
    path('cart/sup<int:my_id>/',del_prod_card,name='del_prod_card'),

    # url pour afficher tout les produits dans index2
    path('',list_menu,name='list_menu'),
    # url du panier
    path('cart/',cart,name='cart'),
    # url pour afficher tout les produits dans all
    path('all_products',all_products,name='all_products'),
    # url pour afficher la categorie desserts
    path('categorie<int:id_categorie>',aff_categories,name='categorie'),
    # url pour afficher les recherches
    path('recherche',recherche,name='recherche'),
    # url pour les commentaires
    path('contact',contact,name='contact'),
    path('apropos',apropos,name='apropos'),
    # url pour reservation
    path('reservation',reservation,name='reservation'),
     

    
]
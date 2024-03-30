from django.contrib import admin
from .models import Produits,Categorie,Order,Card,Commentaires,Reservation
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom','prix','date','categorie')
    search_fields = ('nom','categorie')
    ordering = ('date',)

# Register your models here.
admin.site.register(Produits, ArticleAdmin)
admin.site.register(Categorie)
admin.site.register(Order)
admin.site.register(Card)
admin.site.register(Commentaires)
admin.site.register(Reservation)


admin.site.site_title=("Bienvenu dans mon site E-commerce") # pour chager le titre au niveau du login admin
admin.site.index_title=("LeRoiDuClavier")# pour changer le titre du titre
admin.site.site_header=("Bienvenu dans mon site E-commerce")# pour changer l'entete du site
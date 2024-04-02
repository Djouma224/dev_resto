from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import admin
from .models import Produits,Categorie,Order,Card,Commentaires,Reservation
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom','prix','date','categorie')
    search_fields = ('nom','categorie')
    ordering = ('date',)
    

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('client', 'date','heure','reservation','statu')
    actions = ['confirmer_reservation','annuler_reservation']

    def confirmer_reservation(self, request, queryset):
        for reservation in queryset:
            reservation.statu = 'confirmée'
            reservation.save()
            subject = 'Confirmation reservation'
            message = "votre reservation a été confirmé"
            from_email = settings.EMAIL_HOST_USER
            to_email = reservation.client.email
            email = EmailMessage(subject,message,from_email,[to_email])
            email.send()
        self.message_user(request, "Les réservations sélectionnées ont été confirmées avec succès.")
    confirmer_reservation.short_description = "Confirmer les réservations sélectionnées"
    
    
    def annuler_reservation(self, request, queryset):
        for reservation in queryset:
            reservation.statu = 'annulée'
            reservation.save()
            subject = 'Annulation de la réservation'
            message = "Votre réservation a été annulée"
            from_email = settings.EMAIL_HOST_USER
            to_email = reservation.client.email
            email = EmailMessage(subject, message, from_email, [to_email])
            email.send()
        self.message_user(request, "Les réservations sélectionnées ont été annulées avec succès.")
    annuler_reservation.short_description = "Annuler les réservations sélectionnées"

# Register your models here.
admin.site.register(Produits, ArticleAdmin)
admin.site.register(Categorie)
admin.site.register(Order)
admin.site.register(Card)
admin.site.register(Commentaires)
admin.site.register(Reservation, ReservationAdmin)


admin.site.site_title=("Bienvenu dans mon site E-commerce") # pour chager le titre au niveau du login admin
admin.site.index_title=("LeRoiDuClavier")# pour changer le titre du titre
admin.site.site_header=("Bienvenu dans mon site E-commerce")# pour changer l'entete du site
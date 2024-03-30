from django.contrib.auth import views
from django.urls import path
from gestion_compte.views import reset_password, singup,logout_user,login_user,password_change
# a importer pour le reset_password
# from django.contrib.auth import views


urlpatterns = [
    path('singup/',singup,name='singup'),
    path('logout/',logout_user,name='logout'),
    path('login/',login_user,name='login'),
    # url pour la reinitialisation de mot de passe:
    path('password/auth/reset',reset_password,name='reset_password'),
    path('password/auth/change/<str:token>',password_change,name='password_change'),
    # cette classe se charde d'envoyer le lien ou on va entre notre Email ou on doit envoyer votre le message de reinitialisation
    # path('reset_password',views.PasswordResetView.as_view(template_name="gestion_produit/reset_password.html"),name="reset_password"),#
    # # #  cette classe se charge d'envoyer le mail
    # path('reset_password_sent',views.PasswordResetDoneView.as_view(template_name="gestion_produit/reset_password_sent.html"),name="password_reset_done"),
    # path('reset/<uidb64>/<token>',views.PasswordResetConfirmView.as_view(template_name="gestion_produit/reset_password_form.html"),name="password_reset_confirm"),
    # path('reset_password_complete',views.PasswordResetCompleteView.as_view(template_name="gestion_produit/reset_password_done.html"),name="password_reset_complete"),
    
]
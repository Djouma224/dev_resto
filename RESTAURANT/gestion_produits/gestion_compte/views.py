from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate # a importer et elle permet de recuperer notre model d'utilisateur pour gerer les utilisateurs dans notre cas ce le model ustilisateurs
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from .models import utilisateurs
import secrets
from django.conf import settings
from django.core.mail import EmailMessage
# User = get_user_model() # permet de rcuperer la classe "utilisateurs"
#fn de creation de compte utilisateur
def singup(request):
    if request.method == "POST":
        # traiter le formulaire
        # recuperer les infos du formulaire de l'utilisateur
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        token = secrets.token_urlsafe(32)
        # creer un utilisateurs et le recuperer dans la variable "user"
        user = utilisateurs.objects.create_user(username=username,
                                 password=password,
                                 phone=phone,
                                 email=email,
                                 profile=image,
                                 token=token                  
                                                            
                                 )
        # if image:
        #     user.profile=image
        user.save()
        login(request,user) #connecter l'utilisateur il faut import la fonction "login() dans django.contrib.aut"
                #cette fonction a comme parametre request et la variable qui contient l'utilisateur creer precedement "user"
        return redirect('login') # redirige l'utilisateur sur la page de connexion

    return render(request, 'gestion_compte/singup.html')
# fn de deconnexion il faut importer la fn logout
def logout_user(request):
    logout(request)
    return redirect('list_menu')

# fn d'authentification
def login_user(request):
    if request.method == "POST":
        # connecter l'utilisateur
        # recuperer dabord les informations de l'utilisateur
        username = request.POST.get('username')
        password = request.POST.get('password')

        # cette fn permet de verifier que les informations de l'utilisateur sont les bonnes elle est disponible dans meme module que login()
        # la fonction recupère les infos dans la variable "user" pour les manipuler
        user = authenticate(username=username, password=password)
        # si l'authentification a reussi de connecter
        if user:
            login(request,user)
            # ensuite on le redirige vers la page d'accueil 
            return redirect('all_products')
        return render(request, 'gestion_compte/login.html')
    return render(request, 'gestion_compte/login.html')

def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email_reset')
        user = utilisateurs.objects.filter(email=email)
        if user:
            token = user[0].token
            subject = 'Changement de mot de passe'
            message = f"Cliquer sur ce lien pour changer votre mot de passe http://127.0.0.1:8000/password/auth/change/{token}"
            from_email = settings.EMAIL_HOST_USER
            to_email = email
            email = EmailMessage(subject,message,from_email,[to_email])
            email.send()
            info = f"Un lien viens d'etre envoyer dans votre boite mail cliquer pour changer votre mot de passe"
            return render(request,'gestion_produit/reset_password.html',{"info":info})
        else:
            error = f"Adresse email saisie est incorrecte"
            return render(request,'gestion_produit/reset_password.html',{"error":error})
    return render(request,'gestion_produit/reset_password.html')


def password_change(request,token):
    if request.method == 'POST':
        new_pwd = request.POST.get('new_pwd')
        users = utilisateurs.objects.filter(token=token)
        user=users[0]
        user.set_password(new_pwd)
        user.save()
        return redirect('login')
    return render(request,'gestion_produit/change_password_.html')
    
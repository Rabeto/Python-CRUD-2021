from django.shortcuts import render,redirect,HttpResponse
from .models import Collection

# Create your views here.
def index(request):
    Collections = Collection.objects.all()
    context = {
        'Collections': Collections
    }
    return render(request,'index.html',context)

def create(request):
    print(request.POST)
    titre = request.GET['titre']
    realisateur = request.GET['realisateur']
    contenu = request.GET['contenu']
    date = request.GET['date']
    categorie = request.GET['categorie']
    create_collec = Collection(Titre=titre,Realisateur=realisateur,Contenu=contenu,Date=date,Categorie=categorie)
    create_collec.save()
    return redirect('/index')

def add_collection(request):
    return render(request,'add_collection.html')

def delete(request,id):
    Collections = Collection.objects.get(pk=id)
    Collections.delete()
    return redirect('/index')

def edit(request,id):
    Collections = Collection.objects.get(pk=id)
    context = {
        'Collections': Collections
    }
    return render(request,'edit.html',context)

def update(request,id):
    Coll = Collection.objects.get(pk=id)
    Coll.Titre = request.GET['titre']
    Coll.Realisateur = request.GET['realisateur']
    Coll.Contenu = request.GET['contenu']
    Coll.Date = request.GET['date']
    Coll.Categorie = request.GET['categorie']
    Coll.save()
    return redirect('/index')

def pie_chart(request):
    category = []
    nb_F = Collection.objects.filter(Categorie="Films").count()
    nb_S = Collection.objects.filter(Categorie="Séries").count()
    nb_L = Collection.objects.filter(Categorie="Livres").count()
    nb_J = Collection.objects.filter(Categorie="Jeux").count()
    context = {
        'nb_F': nb_F,
        'nb_S': nb_S,
        'nb_L': nb_L,
        'nb_J': nb_J
    }
    return render(request,'pie_chart.html',context)
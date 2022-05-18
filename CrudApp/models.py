from django.db import models

# Create your models here.
class Collection(models.Model):
    Titre = models.CharField(max_length=100)
    Realisateur = models.CharField(max_length=42)
    Contenu = models.TextField(null=True)
    Date = models.DateField()
    Categorie = models.CharField(max_length=64)

    def __str__(self):
        return self.Titre


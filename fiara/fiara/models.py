from django.db import models

class Personne(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255,null=False)
    prenom = models.CharField(max_length=255,null=False)
    age = models.IntegerField(null=False)
    genre = models.CharField(max_length=50, null=True)
    
    nom_modifier = models.CharField(max_length=100, blank=True, null=True)
    prenom_modifier = models.CharField(max_length=100, blank=True, null=True)
    age_modifier = models.IntegerField(blank=True, null=True)


class Voiture(models.Model):
    immatriculation = models.CharField(max_length=8, primary_key=True)
    marque = models.CharField(max_length=255, null=False)
    proprietaire = models.ForeignKey(Personne, on_delete=models.CASCADE,null=False)
    image = models.CharField(max_length=255,null=False)
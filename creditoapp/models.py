from django.db import models

# Create your models here.


class Organisatie(models.Model):
    naam = models.CharField(max_length=150, db_index=True)

    class Meta:
        ordering = ('naam',)
        verbose_name = 'organisatie'

    def __str__(self):
        return self.naam


class Werknemer(models.Model):
    organisatie = models.ForeignKey(Organisatie, related_name='werknemers', default=None)
    voornaam = models.CharField(max_length=150)
    tussenvoegsel = models.CharField(max_length=5, blank=True)
    achternaam = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    wachtwoord = models.CharField(max_length=50, blank=True)
    nieuwwachtwoord = models.CharField(max_length=50, blank=True)
    rol = models.CharField(max_length=150, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.voornaam











from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa")

    def __str__(self):
        return self.name


class Institution(models.Model):
    TYPE_CHOICES = [
        (1, 'Fundacja'),
        (2, 'Organizacja pozarządowa'),
        (3, 'Zbiórka lokalna'),
    ]
    name = models.CharField(max_length=255, verbose_name="Nazwa instytucji")
    description = models.TextField(verbose_name="Opis")
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, verbose_name="Typ", default=1)
    categories = models.ManyToManyField(Category, verbose_name="Kategorie")

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField(verbose_name="Liczba worków")
    categories = models.ManyToManyField(Category, verbose_name="Kategorie")
    institution = models.ForeignKey(Institution, verbose_name="Instytucja", on_delete=models.CASCADE)
    address = models.CharField(max_length=255, verbose_name="Adres")
    phone_number = models.CharField(max_length=15, verbose_name="Numer telefonu")
    city = models.CharField(max_length=100, verbose_name="Miasto")
    zip_code = models.CharField(max_length=6, verbose_name="Kod pocztowy")
    pick_up_date = models.DateField(verbose_name="Data odbioru")
    pick_up_time = models.TimeField(verbose_name="Godzina odbioru")
    pick_up_comment = models.TextField(blank=True, verbose_name="Komentarz do odbioru")
    user = models.ForeignKey(User, verbose_name="Użytkownik", on_delete=models.SET_NULL, null=True, blank=True)
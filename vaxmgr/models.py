# coding=utf8
from django.db import models
from django_currentuser.db.models import CurrentUserField


class Vaccine(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nazwa szczepionki')
    description = models.TextField(max_length=500, verbose_name='Opis')
    illness = models.TextField(max_length=100, verbose_name='Przeciw')

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nazwa placówki')
    city = models.CharField(max_length=50, verbose_name='Miasto', default='Warszawa')

    def __unicode__(self):
        return self.city.decode('utf-8')
    def __str__(self):
        return self.name


class Connection(models.Model):
    vaccine = models.ForeignKey('Vaccine', on_delete=models.CASCADE, verbose_name='Szczepionka')
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, verbose_name='Placówka')
    date = models.DateField(auto_now=True, editable=False)
    amount = models.IntegerField(default=0, verbose_name='Ilość')
    modified_by = CurrentUserField()

    def __str__(self):
        return self.vaccine.name + ' w oddziale ' + self.branch.name

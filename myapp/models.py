from django.db import models

# Create your models here.
class Bliblioteca(models.Model):
    '''modelo para las bibliotecas'''
    name = models.CharField(max_length=50, help_text='ingrese el nombre de la biblioteca.')
    direction = models.CharField(max_length=50, help_text='ingrese la direccion de la biblioteca')

class Libro(models.Model):
    '''modelo de los libros'''
    biblioteca = models.ForeignKey(Bliblioteca, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, help_text='ingrese el nombre del libro')
    isbn = models.CharField(max_length=13, help_text='ingrese el ISBN del libro')
    autor = models.CharField(max_length=50, help_text='ingrese el autor del libro')
    done = models.CharField(max_length=8,help_text='ingrese si el libro esta prestado o en sala')
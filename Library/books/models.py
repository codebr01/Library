from django.db import models


class Book(models.Model):
    
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    paginas = models.IntegerField()
    ano = models.IntegerField()

    def __str__(self):
        return self.titulo
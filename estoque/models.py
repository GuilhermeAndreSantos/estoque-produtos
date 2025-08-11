from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Estoque(models.Model):
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    quantidade_estoque = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE
                                  )

    def __str__(self):
        return f"{self.nome} ({self.quantidade_estoque}un.)"

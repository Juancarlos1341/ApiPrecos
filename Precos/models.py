from django.db import models

class Precos(models.Model):

    Codigo = models.IntegerField()
    Produto = models.CharField(max_length=255)
    VlrCompra = models.CharField(max_length=255)
    VlrVenda = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.Produto

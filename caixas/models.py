from django.db import models

class CaixasHf(models.Model):

    Codigo = models.CharField(max_length=20)
    DataInicial = models.CharField(max_length=20)
    HoraInicial = models.CharField(max_length=20)
    SaldoInicial = models.CharField(max_length=100, default=0)
    TotalVendas = models.CharField(max_length=100, default=0)
    Dinheiro = models.CharField(max_length=100, default=0)
    Pix = models.CharField(max_length=100, default=0)
    CartaoCredito = models.CharField(max_length=100, default=0)
    CartaoDebito = models.CharField(max_length=100, default=0)
    Cheque = models.CharField(max_length=100, default=0) 
    Sangria = models.CharField(max_length=100, default=0)
    SomaTotalCaixa = models.CharField(max_length=100, default=0)
    TotalCaixa = models.CharField(max_length=100, default=0)
    VendasPrazo = models.CharField(max_length=100, default=0)
    Despesas = models.CharField(max_length=100, default=0)
    DataFinal = models.CharField(max_length=20)
    HoraFinal = models.CharField(max_length=20)
    Operador = models.CharField(max_length=20)
    VendasRecebidas = models.CharField(max_length=100, default=0)
    Desconto = models.CharField(max_length=100, default=0)
    EntradaDeNotas = models.CharField(max_length=100, default=0)
    
    def __str__(self) -> str:
        return self.DataInicial


class CaixasSm(models.Model):

    Codigo = models.CharField(max_length=20)
    DataInicial = models.CharField(max_length=20)
    HoraInicial = models.CharField(max_length=20)
    SaldoInicial = models.CharField(max_length=100, default=0)
    TotalVendas = models.CharField(max_length=100, default=0)
    Dinheiro = models.CharField(max_length=100, default=0)
    Pix = models.CharField(max_length=100, default=0)
    CartaoCredito = models.CharField(max_length=100, default=0)
    CartaoDebito = models.CharField(max_length=100, default=0)
    Cheque = models.CharField(max_length=100, default=0)
    Sangria = models.CharField(max_length=100, default=0)
    SomaTotalCaixa = models.CharField(max_length=100, default=0)
    TotalCaixa = models.CharField(max_length=100, default=0)
    DataFinal = models.CharField(max_length=20)
    HoraFinal = models.CharField(max_length=20)
    Operador = models.CharField(max_length=20)
    VendasRecebidas = models.CharField(max_length=100, default=0)
    Desconto = models.CharField(max_length=100, default=0)
    EntradaDeNotas = models.CharField(max_length=100, default=0)
    VendasAPrazo = models.CharField(max_length=100, default=0)

    def __str__(self) -> str:
        return self.DataInicial

class Sangria_Hf(models.Model):
    Codigo = models.CharField(max_length=100, default='0')
    Codigo_caixa = models.CharField(max_length=20, default='0')
    Data = models.CharField(max_length=20, default='1/1/23')
    Dinheiro = models.CharField(max_length=100, default=0)
    Cheque = models.CharField(max_length=100, default=0)
    Total = models.CharField(max_length=100, default=0)
    Descriacao = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Descriacao

class Sangria_Sm(models.Model):
    Codigo = models.CharField(max_length=100, default='0')
    Codigo_caixa = models.CharField(max_length=20, default='0')
    Data = models.CharField(max_length=20, default='1/1/23')
    Dinheiro = models.CharField(max_length=100, default=0)
    Cheque = models.CharField(max_length=100, default=0)
    Total = models.CharField(max_length=100, default=0)
    Descriacao = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Descriacao

class Entrada_de_notas_Hf(models.Model):
    Codigo = models.CharField(max_length=100, default='0')
    DataEmissão = models.CharField(max_length=20, default='1/1/23')
    Fornecedor = models.CharField(max_length=100)
    TotalPagar = models.CharField(max_length=100, default=0)
    TipoDeEntrada = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Fornecedor

class Entrada_de_notas_Sm(models.Model):
    Codigo = models.CharField(max_length=100, default='0')
    DataEmissão = models.CharField(max_length=20, default='1/1/23')
    Fornecedor = models.CharField(max_length=100)
    TotalPagar = models.CharField(max_length=100, default=0)
    TipoDeEntrada = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Fornecedor
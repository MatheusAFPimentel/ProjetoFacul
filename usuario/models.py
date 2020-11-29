from django.db import models

class Usuario(models.Model):
    Nome_completo = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    CEP = models.PositiveIntegerField()
    Telefone = models.PositiveIntegerField()
    Nome_da_rua = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=100)
    Estado = models.CharField(max_length=100)
    Ponto_de_referencia = models.CharField(max_length=100)
    Bairro = models.CharField(max_length=100)
    Sexo = models.CharField(max_length=100)
    CPF = models.PositiveIntegerField()
    Numero_de_usuario =models.PositiveIntegerField()
    Senha = models.PositiveIntegerField()

    def __str__(self):
        return self.Nome_completo
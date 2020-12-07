from django.db import models

class Denuncia(models.Model):
    Nome_da_rua = models.CharField(max_length=100)
    Bairro = models.CharField(max_length=100)
    Ponto_de_referencia = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=100)
    Estado = models.CharField(max_length=100)
    CEP = models.PositiveIntegerField()
    Problematica = models.CharField(max_length=100)
    Titulo = models.CharField(max_length=100)
    Codigo_De_Denuncia = models.PositiveIntegerField()
    Campo_De_Texto = models.CharField(max_length=100)
    Anexar_Imagens = models.FileField(upload_to='photos', blank=True)

    def __str__(self):
        return self.Titulo

        
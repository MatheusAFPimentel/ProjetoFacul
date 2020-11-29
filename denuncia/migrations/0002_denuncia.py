
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_da_rua', models.CharField(max_length=100)),
                ('Bairro', models.CharField(max_length=100)),
                ('Ponto_de_referencia', models.CharField(max_length=100)),
                ('Cidade', models.CharField(max_length=100)),
                ('Estado', models.CharField(max_length=100)),
                ('CEP', models.PositiveIntegerField()),
                ('Problematica', models.CharField(max_length=100)),
                ('Titulo', models.CharField(max_length=100)),
                ('Codigo_De_Denuncia', models.CharField(max_length=100)),
                ('Campo_De_Texto', models.PositiveIntegerField()),
                ('Anexar_Imagens', models.FileField()),
            ],
        ),
    ]

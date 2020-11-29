
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_completo', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('CEP', models.PositiveIntegerField()),
                ('Telefone', models.PositiveIntegerField()),
                ('Nome_da_rua', models.CharField(max_length=100)),
                ('Cidade', models.CharField(max_length=100)),
                ('Estado', models.CharField(max_length=100)),
                ('Ponto_de_referencia', models.CharField(max_length=100)),
                ('Bairro', models.CharField(max_length=100)),
                ('Sexo', models.CharField(max_length=100)),
                ('CPF', models.PositiveIntegerField()),
                ('Numero_de_usuario', models.PositiveIntegerField()),
                ('Senha', models.PositiveIntegerField()),
            ],
        ),
    ]

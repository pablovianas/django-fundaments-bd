# Generated by Django 4.0.3 on 2022-03-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_cliente_endereco_alter_cliente_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('O', 'Outra opção'), ('M', 'Masculino'), ('F', 'Feminino')], max_length=1),
        ),
    ]

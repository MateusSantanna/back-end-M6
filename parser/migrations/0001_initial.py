# Generated by Django 4.1.5 on 2023-01-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="InfoModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo", models.CharField(max_length=1)),
                ("data", models.CharField(max_length=8)),
                ("valor", models.CharField(max_length=10)),
                ("cpf", models.CharField(max_length=11)),
                ("cartao", models.CharField(max_length=12)),
                ("hora", models.CharField(max_length=6)),
                ("dono", models.CharField(max_length=14)),
                ("loja", models.CharField(max_length=19)),
            ],
        ),
        migrations.CreateModel(
            name="ParsedModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("debito entrada", "Debito"),
                            ("boleto saida", "Boleto"),
                            ("financiamento saida", "Financiamento"),
                            ("credito entrada", "Credito"),
                            ("recebimento emprestimo entrada", "Emprestimo"),
                            ("vendas entrada", "Vendas"),
                            ("recebimento ted entrada", "Ted"),
                            ("recebimento doc entrada", "Doc"),
                            ("aluguel saida", "Aluguel"),
                        ],
                        default=None,
                        max_length=255,
                    ),
                ),
                ("data", models.DateField()),
                ("valor", models.IntegerField()),
                ("cpf", models.CharField(max_length=11)),
                ("cartao", models.CharField(max_length=12)),
                ("hora", models.TimeField()),
                ("dono", models.CharField(max_length=14)),
                ("loja", models.CharField(max_length=19)),
            ],
        ),
    ]
from django.db import models

class Om(models.Model):
    LISTA_OMS = (
        ('PMPV', 'PMPV'),
        ('PMRJ', 'PMRJ'),
        ('PMN', 'PMN'),
        ('IBEX', 'IBEX'),
        ('HCE', 'HCE'),
        ('OCEX', 'OCEX'),
        ('HMR', 'HMR'),
        ('HGERJ', 'HGERJ'),
        ('PM Gu VV', 'PM Gu VV'),
        ('LQFEX', 'LQFEX'),
        )

    sigla = models.CharField(max_length=10, choices=LISTA_OMS)
    foto = models.ImageField(upload_to="imagens")
    email = models.EmailField(null=True)
    telefone = models.IntegerField(null=True)

    def __str__(self):
        return self.sigla


class Empenho(models.Model):
    LISTA_ND = (
        ("30", '30'),
        ("39", '30'),
        ("52", '30'),
    )

    LISTA_UG = (
        ("160242", '160242'),
        ("167242", '167242'),
    )

    LISTA_FORNECEDOR = (
        ('BIOMEDICAL', 'BIOMEDICAL'),
        ('SULAR', 'SULAR'),
        ('MEDSANTA', 'MEDSANTA'),
    )

    om = models.ForeignKey(Om, on_delete=models.CASCADE)
    fornecedor = models.CharField(max_length=50, choices=LISTA_FORNECEDOR)
    nd = models.CharField(max_length=2,choices=LISTA_ND)
    ug = models.CharField(max_length=6,choices=LISTA_UG)
    pregao = models.CharField(max_length=8)
    data = models.DateField()
    numero = models.IntegerField()
    pdf = models.FileField(upload_to="pdf")
    

    def __str__(self):
        return self.fornecedor

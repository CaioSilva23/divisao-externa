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
    foto = models.ImageField(upload_to="logo_om")
    email = models.EmailField(null=True)
    telefone = models.IntegerField(null=True)
    ch_almox = models.CharField(max_length=10, null=True, blank=True)
    tel_ch_almox = models.CharField(max_length=15, null=True, blank=True)
    adj_almox = models.CharField(max_length=10, null=True, blank=True)
    tel_adj_almox = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.sigla


from django.db import models

class Om(models.Model):
    LISTA_OMS = (
        ('PMPV', 'PMPV'),
        ('PMRJ', 'PMRJ'),
        ('PMN', 'PMN'),
        ('IBEX', 'IBEX'),
        ('HCE', 'HCE'),
        ('OCEX', 'OCEX'),
        )

    sigla = models.CharField(max_length=10, choices=LISTA_OMS)
    descricao = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="imagens")
    email = models.EmailField(null=True)
    telefone = models.CharField(max_length=19, null=True)

    def __str__(self):
        return self.sigla

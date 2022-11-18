from django.db import models
from datetime import date
from django.utils.timezone import now
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
    ch_almox = models.CharField(max_length=10, null=True, blank=True)
    tel_ch_almox = models.CharField(max_length=15, null=True, blank=True)
    adj_almox = models.CharField(max_length=10, null=True, blank=True)
    tel_adj_almox = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.sigla


class Fornecedor(models.Model):
    nome = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome




class Pregao(models.Model):
    SITUACAO_CHICES = (
    ('HOMOLOGADO','HOMOLOGADO'),
    ('CJU','CJU'),
    )

    numero_ano = models.CharField(max_length=7)
    situacao = models.CharField(max_length=20, choices=SITUACAO_CHICES)
    descrição = models.CharField(max_length=200)
    oms_favorecidas = models.ManyToManyField(Om)
    termo_homolocao = models.URLField()
    catalago = models.FileField(upload_to='catalago', null=True, blank=True)
    
    
    def __str__(self):
        return self.numero_ano


class Empenho(models.Model):
    om = models.ForeignKey(Om, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    pregao = models.ForeignKey(Pregao, on_delete=models.DO_NOTHING)
    data = models.DateField()
    numero = models.CharField(max_length=4)
    pdf = models.FileField(upload_to="pdf")
    

    def __str__(self):
        return f'2022NE000{self.numero}'


class PlanoInterno(models.Model):
    pi = models.CharField(max_length=15)
  
    def valor_total(self):
        creditos = NotaCredito.objects.filter(pi_id=self.id)
        total = 0
        for i in creditos:
            total += i.valor
        return total

    def __str__(self):
        return self.pi


class NotaCredito(models.Model):
    numero = models.CharField(max_length=10)
    valor = models.FloatField()
    fonte = models.CharField(max_length=10)
    nd = models.CharField(max_length=6)
    pi = models.ForeignKey(PlanoInterno, on_delete=models.CASCADE)

    def __str__(self):
        return f'2022NC{self.numero}'
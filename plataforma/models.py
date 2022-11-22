from django.db import models
from datetime import date
from django.db.models.aggregates import Avg, Sum, Min, Max

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

    saldo_homologado = models.FloatField()
    pregao = models.CharField(max_length=7, null=False, blank=False)
    situacao = models.CharField(max_length=20, choices=SITUACAO_CHICES)
    descrição = models.CharField(max_length=200, null=False, blank=False)
    oms_favorecidas = models.ManyToManyField(Om)
    termo_homolocao = models.URLField()
    catalago = models.FileField(upload_to='catalago', null=True, blank=True)
    
    def __str__(self):
        return self.pregao

class PlanoInterno(models.Model):
    pi = models.CharField(max_length=15)
  
    def valor_total(self):
        creditos = NotaCredito.objects.filter(pi_id=self.id).aggregate(Sum('valor'))
        valor  = f"{creditos['valor__sum']:_.2f}"
        return valor.replace('.',',').replace('_','.')

    def __str__(self):
        return self.pi


class NotaCredito(models.Model):
    numero = models.CharField(max_length=10)
    valor = models.FloatField()
    fonte = models.CharField(max_length=10)
    nd = models.CharField(max_length=6)
    pi = models.ForeignKey(PlanoInterno, on_delete=models.SET_NULL, null=True)


    def saldo(self):
        saldo = f'{self.valor:_.2f}'
        return saldo.replace('.',',').replace('_','.')

    def saldo_empenhado(self):
        empenhos = Empenho.objects.filter(nota_credito_id=self.id).aggregate(Sum('valor'))['valor__sum']
        if not empenhos:
            return 0
        return f"{empenhos:_.2f}".replace('.',',').replace('_','.')

    def disponivel(self):
        empenhos = Empenho.objects.filter(nota_credito_id=self.id).aggregate(Sum('valor'))['valor__sum']
        saldo = self.valor
        if not empenhos:
            return f'{saldo:_.2f}'.replace('.',',').replace('_','.')
        return f'{saldo - empenhos:_.2f}'.replace('.',',').replace('_','.')

    
    def __str__(self):
        return f'2022NC{self.numero}'

class Empenho(models.Model):
    om = models.ForeignKey(Om, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)
    pregao = models.ForeignKey(Pregao, on_delete=models.SET_NULL, null=True)
    plano_interno = models.ForeignKey(PlanoInterno, on_delete=models.SET_NULL, null=True)
    nota_credito = models.ForeignKey(NotaCredito, on_delete=models.SET_NULL, null=True)
    data = models.DateField()
    numero = models.CharField(max_length=4)
    pdf = models.FileField(upload_to="pdf", null=True, blank=True)
    valor = models.FloatField(null=True, blank=True)
    


    def __str__(self):
        return f'2022NE000{self.numero}'


class Arquivo(models.Model):
    demanda = models.FileField(upload_to='demanda-oms')
    om = models.ForeignKey(Om, on_delete=models.CASCADE)
    data = models.DateField(default=date.today())

    def __str__(self) -> str:
        return 'Aquivo'

    
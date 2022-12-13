from django.db import models
from django.db.models.aggregates import Avg, Sum, Min, Max
from django.utils.timezone import now


from oms.models import Om
from empenhos.models import Empenho


class Fornecedor(models.Model):
    nome = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome

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
        saldo = f'{self.valor:_.2f}'.replace('.',',').replace('_','.')
        return saldo

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




class Arquivo(models.Model):
    demanda = models.FileField(upload_to='demanda-oms', null=True)
    om = models.ForeignKey(Om, on_delete=models.CASCADE)
    data = models.DateField(default=now)

    def __str__(self) -> str:
        return 'Aquivo'

    
from django.db import models
from datetime import date, datetime
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from oms.models import Om




class Empenho(models.Model):
    om = models.ForeignKey(Om, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey("plataforma.Fornecedor", on_delete=models.SET_NULL, null=True)
    pregao = models.ForeignKey("pregoes.Pregao", on_delete=models.SET_NULL, null=True)
    plano_interno = models.ForeignKey("plataforma.PlanoInterno", on_delete=models.SET_NULL, null=True)
    nota_credito = models.ForeignKey("plataforma.NotaCredito", on_delete=models.SET_NULL, null=True)
    data = models.DateField()
    numero = models.CharField(max_length=4)
    pdf = models.FileField(upload_to="empenhos", null=True, blank=True)
    valor = models.FloatField(null=True, blank=True)
    entregue = models.BooleanField(default=False)


    def qtd_dias(self):
        # Data final
        data = str(date.today())

        d2 = datetime.strptime(data, '%Y-%m-%d')
        # Data inicial
        d1 = datetime.strptime(str(self.data), '%Y-%m-%d')

        # Realizamos o calculo da quantidade de dias
        quantidade_dias = abs((d2 - d1).days)
        
        return quantidade_dias


    def prioridade(self):
        if self.qtd_dias() < 30:
            classe = "table-success"
        elif self.qtd_dias() <= 50:
            classe = "table-warning"
        else:
            classe = "table-danger"
        prioridade = f'''class="{classe}"'''

        return mark_safe(str(prioridade))
        
    def preco(self):
        preco = f'{self.valor:_.2f}'.replace('.',',').replace('_','.')
        return preco

    def __str__(self):
        return f'2022NE000{self.numero}'

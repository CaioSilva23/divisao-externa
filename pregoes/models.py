from django.db import models



class Pregao(models.Model):
    SITUACAO_CHICES = (
    ('HOMOLOGADO','HOMOLOGADO'),
    ('CJU','CJU'),
    )

    saldo_homologado = models.FloatField()
    pregao = models.CharField(max_length=7, null=False, blank=False)
    situacao = models.CharField(max_length=20, choices=SITUACAO_CHICES)
    descrição = models.CharField(max_length=200, null=False, blank=False)
    oms_favorecidas = models.ManyToManyField("oms.Om")
    termo_homolocao = models.URLField()
    catalago = models.FileField(upload_to='catalago', null=True, blank=True)
    
    def __str__(self):
        return self.pregao
    
    def saldo(self):
        saldo = f'{self.saldo_homologado:_.2f}'

        return saldo.replace('.',',').replace('_','.')
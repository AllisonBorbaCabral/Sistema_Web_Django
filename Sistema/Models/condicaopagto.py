from django.db import models


class condicao_pagto(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    ds_condicao_pagto = models.CharField(
        db_column='DS_CONDICAO_PAGTO', max_length=255, null=False, verbose_name='Condição de Pagamento')
    multa = models.DecimalField(
        db_column='MULTA', max_digits=19, decimal_places=2, null=False, verbose_name='Multa')
    juros = models.DecimalField(
        db_column='JUROS', max_digits=19, decimal_places=2, null=False, verbose_name='Juros')
    desc_financeiro = models.DecimalField(
        db_column='DESC_FINANCEIRO', max_digits=19, decimal_places=2, null=False, verbose_name='Desconto Financeiro')
    dt_cadastro = models.DateTimeField(
        db_column='DT_CADASTRO', auto_now=True, null=False)
    dt_ult_alt = models.DateTimeField(
        db_column='DT_ULT_ALTERACAO', auto_now=False, null=False)

    def getCondicaoPagto(self):
        return (f'{self.ds_condicao_pagto}')

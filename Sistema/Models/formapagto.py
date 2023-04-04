from django.db import models


class forma_pagto(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    ds_forma_pagto = models.CharField(
        db_column='DS_FORMA_PAGTO', max_length=255, null=False, verbose_name='Forma de Pagamento')
    situacao = models.CharField(
        db_column='SITUACAO', max_length=1, null=False, verbose_name='Situação')
    dt_cadastro = models.DateTimeField(
        db_column='DT_CADASTRO', auto_now=True, null=False)
    dt_ult_alt = models.DateTimeField(
        db_column='DT_ULT_ALTERACAO', auto_now=False, null=False)

    def getFormaPagto(self):
        return (f'{self.ds_forma_pagto}')

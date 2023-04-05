from django.db import models


class tamanho(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    ds_tamanho = models.CharField(db_column='DS_TAMANHO',
                                  null=False, max_length=10, verbose_name='TAMANHO')
    dt_cadastro = models.DateTimeField(
        db_column='DT_CADASTRO', auto_now=True, null=False)
    dt_ult_alt = models.DateTimeField(
        db_column='DT_ULT_ALTERACAO', auto_now=False, null=False)

    def getID(self):
        return (f'{self.id}')

    def getTamanho(self):
        return (f'{self.ds_tamanho}')

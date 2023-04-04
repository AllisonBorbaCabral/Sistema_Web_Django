from django.db import models

from . import estado


class cidade(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nm_cidade = models.CharField(
        db_column='NM_CIDADE', max_length=100, null=False, verbose_name='Cidade')
    ddd = models.CharField(db_column='DDD', max_length=2, null=False)
    estado = models.ForeignKey(estado.estado, db_column='ID_ESTADO',
                               null=False, on_delete=models.PROTECT, verbose_name='Estado')
    dt_cadastro = models.DateTimeField(
        db_column='DT_CADASTRO', auto_now=True, null=False)
    dt_ult_alt = models.DateTimeField(
        db_column='DT_ULT_ALTERACAO', auto_now=False, null=False,)

    def getId(self):
        return (f'{self.id}')

    def getCidade(self):
        return (f'{self.nm_cidade}')

    def getDDD(self):
        return (f'{self.ddd}')

    def getEstado(self):
        return (f'{self.estado.nm_estado}')

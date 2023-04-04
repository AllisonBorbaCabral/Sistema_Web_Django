from django.db import models

from . import pais


class estado(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nm_estado = models.CharField(
        db_column='NM_ESTADO', max_length=100, null=False, verbose_name='Estado')
    uf = models.CharField(db_column='UF', max_length=2,
                          null=False, verbose_name='UF')
    pais = models.ForeignKey(pais.pais, db_column='ID_PAIS',
                             null=False, on_delete=models.PROTECT, verbose_name='País')
    dt_cadastro = models.DateTimeField(
        db_column='DT_CADASTRO', auto_now=True, null=False)
    dt_ult_alt = models.DateTimeField(
        db_column='DT_ULT_ALTERACAO', auto_now=False, null=False,)

    def __str__(self):
        return " {} ".format(self.nm_estado)

    def getEstado(self):
        return (f'{self.nm_estado}')

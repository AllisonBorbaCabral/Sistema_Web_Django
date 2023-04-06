from django.db import models


class pais(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nm_pais = models.CharField(
        db_column='NM_PAIS', max_length=100, null=False, verbose_name='País')
    ddi = models.CharField(db_column='DDI', max_length=5,
                           null=False, verbose_name='DDI')
    sigla = models.CharField(db_column='SIGLA', max_length=3, null=False)
    dt_cadastro = models.DateTimeField(
        db_column='DT_CADASTRO', auto_now_add=True, null=False)
    dt_ult_alt = models.DateTimeField(
        db_column='DT_ULT_ALTERACAO', auto_now=False, null=False)

    @property
    def readonly_cadastro(self):
        return self.dt_cadastro

    def readonly_alteracao(self):
        return self.dt_ult_alt

    def __str__(self):
        return " {} ".format(self.nm_pais)

    def getPais(self):
        return (f'{self.nm_pais} - {self.sigla}')

from django.db import models


class pais(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nm_pais = models.CharField(
        db_column='NM_PAIS', max_length=100, null=False, verbose_name='País')
    ddi = models.CharField(db_column='DDI', max_length=5,
                           null=False, verbose_name='DDI')
    sigla = models.CharField(db_column='SIGLA', max_length=3, null=False)
    dt_cadastro = models.DateTimeField(
        db_column='DT_CADASTRO', null=False)
    dt_ult_alteracao = models.DateTimeField(
        db_column='DT_ULT_ALTERACAO', null=False)
    situacao = models.CharField(db_column='SITUACAO', max_length=1, null=False)

    def __str__(self):
        return " {} ".format(self.nm_pais)

    def getPais(self):
        return (f'{self.nm_pais} - {self.sigla}')

    class Meta:
        db_table = 'sistema_pais'

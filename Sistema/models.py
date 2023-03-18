from django.db import models


# Create your models here.
class pais(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nm_pais = models.CharField(db_column='NM_PAIS', max_length=255, null=False)
    ddi = models.CharField(db_column='DDI', max_length=5, null=False)
    sigla = models.CharField(db_column='SIGLA', max_length=3, null=False)
    dt_cadastro = models.DateTimeField(
        db_column='DT_CADASTRO', auto_now=True, null=False)
    dt_ult_alt = models.DateField(
        db_column='DT_ULT_ALTERACAO', auto_now=False, null=False)

    def Pais(self):
        return (f'{self.nm_pais}')

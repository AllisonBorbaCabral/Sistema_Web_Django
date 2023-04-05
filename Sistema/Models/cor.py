from django.db import models


class cor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    ds_cor = models.CharField(
        db_column='DS_COR', max_length=255, null=False, verbose_name='COR')
    situacao = models.CharField(
        db_column='SITUACAO', max_length=1, null=False, verbose_name='SITUAÇÃO')
    dt_cadastro = models.DateTimeField(
        db_column='DT_CADASTRO', auto_now=True, null=False)
    dt_ult_alt = models.DateTimeField(
        db_column='DT_ULT_ALTERACAO', auto_now=False, null=False)

    def getId(self):
        return (f'{self.id}')

    def getCor(self):
        return (f'{self.ds_cor}')

    def getSituacao(self):
        return (f'{self.situacao}').upper()

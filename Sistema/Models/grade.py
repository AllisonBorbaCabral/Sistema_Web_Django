from django.db import models

from . import cor, tamanho


class grade_tamanho(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    dt_cadastro = models.DateTimeField(
        db_column='DT_CADASTRO', auto_now=True, null=False)
    dt_ult_alt = models.DateTimeField(
        db_column='DT_ULT_ALT', auto_now=False, null=False)

    def getID(self):
        return (f'{self.id}')


class tamanho_grade(models.Model):
    id_tamanho = models.ForeignKey(tamanho.tamanho, db_column='ID_TAMANHO', null=False, on_delete=models.PROTECT, verbose_name='TAMANHO' primary_key=True)
    id_grade_tamanho = models.ForeignKey(grade_tamanho, db_column='ID_GRADE_TAMANHO', null=False, on_delete=models.PROTECT, verbose_name='GRADE' primary_key=True)


class grade_cor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    dt_cadastro = models.DateTimeField(
        db_column='DT_CADASTRO', auto_now=True, null=False)
    dt_ult_alt = models.DateTimeField(
        db_column='DT_ULT_ALT', auto_now=True, null=False)

    def getID(self):
        return (f'{self.id}')


class cor_grade(models.Model):
    id_cor = models.ForeignKey(cor.cor, db_column='ID_COR',
                               null=False, on_delete=models.PROTECT, verbose_name='COR', primary_key=True)
    id_grade_cor = models.ForeignKey(grade_cor, db_column='ID_GRADE_COR',
                                     on_delete=models.PROTECT, verbose_name='GRADE', primary_key=True)

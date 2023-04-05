from django.db import models

from . import cidade, cliente


class cliente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nm_pessoa_razao_social = models.CharField(
        db_column='NM_PESSOA_RAZAO_SOCIAL', max_length=255, null=False, verbose_name='NOME/RAZÃO SOCIAL')
    cpf_cnpj = models.CharField(
        db_column='CPF_CNPJ', max_length=14, null=False, verbose_name='CPF/CNPJ')
    rua = models.CharField(
        db_column='RUA', max_length=255, null=False, verbose_name='RUA')
    bairro = models.CharField(
        db_column='BAIRRO', max_length=255, null=False, verbose_name='BAIRRO')
    numero = models.CharField(
        db_column='NUMERO', max_length=255, null=False, verbose_name='NÚMERO')
    complemento = models.CharField(
        db_column='COMPLEMENTO', max_length=255, null=False, verbose_name='COMPLEMENTO')
    cidade = models.ForeignKey(cidade.cidade, db_column='ID_CIDADE',
                               null=False, on_delete=models.PROTECT, verbose_name='CIDADE')
    dt_cadastro = models.DateTimeField(
        db_column='DT_CADASTRO', auto_now=True, null=False)
    dt_ult_alt = models.DateTimeField(
        db_column='DT_ULT_ALTERACAO', auto_now=False, null=False,)

    def __str__(self):
        return " {} ".format(self.nm_pessoa_razao_social)

    def getId(self):
        return (f'{self.id}')

    def getCliente(self):
        return (f'{self.nm_pessoa_razao_social}').upper()

    def getCPFCNPJ(self):
        return (f'{self.cpf_cnpj}')

    def getEndereco(self):
        return (f'{self.rua}, {self.numero} - {self.bairro}, {self.cidade}, {self.cidade.getEstado()}')

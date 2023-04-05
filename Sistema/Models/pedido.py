from django.db import models

from . import cliente


class pedido(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    cliente = models.ForeignKey(cliente.cliente, db_column='ID_CLIENTE',
                                null=False, on_delete=models.PROTECT, verbose_name='CLIENTE')
    dt_pedido = models.DateTimeField(
        db_column='DT_PEDIDO', auto_now=True, null=False)
    dt_cancelamento = models.DateTimeField(
        db_column='DT_CANCELAMENTO', auto_now=False, null=False)

    def getID(self):
        return (f'{self.id}')

    def getCliente(self):
        return (f'{self.cliente.getCliente()}')

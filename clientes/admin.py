from django.contrib import admin
from clientes.models import cliente,saldo_cliente

admin.site.register(cliente)
admin.site.register(saldo_cliente)


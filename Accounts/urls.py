from django.urls import path
from Accounts.views import *

urlpatterns = [

path('dashboard/', dashboard, name='dashboard'),
path('cuentas/', cuentas, name='cuentas'),
path('cuentasFormulario/', cuentasFormulario, name='cuentasFormulario'),

]
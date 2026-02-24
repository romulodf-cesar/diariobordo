from django.urls import path
from professores.views import professores

urlpatterns=[
    path('professores',professores,name='professores')
]
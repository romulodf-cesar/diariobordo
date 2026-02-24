from django.urls import path
from alunos.views import alunos

urlpatterns=[
    path('alunos',alunos,name='alunos')
]
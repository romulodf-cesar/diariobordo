from django.urls import path
from turma.views import turma

urlpatterns=[
    path('turma',turma,name='turma')
]
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('alunos.urls')),
    path('',include('professores.urls')),
    path('',include('diario.urls')),
    path('',include('turma.urls')),
]

"""

+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


"""

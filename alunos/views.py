from django.shortcuts import render

# Create your views here.
def alunos(request):
    return render(request,'alunos/index.html')
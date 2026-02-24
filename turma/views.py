from django.shortcuts import render

# Create your views here.
def turma(request):
    return render(request,'turma/index.html')
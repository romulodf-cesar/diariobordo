from django.shortcuts import render

# Create your views here.
def professores(request):
    return render(request,'professores/index.html')
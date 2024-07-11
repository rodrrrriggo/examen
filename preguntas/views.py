from django.shortcuts import render

# Create your views here.
def preguntas(request):
    context = {}
    return render(request, "preguntas/preguntas.html", context)
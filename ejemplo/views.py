from django.shortcuts import render


def index(request):
    return render(request, "ejemplo/saludar.html", {"nombre":"Diego", "apellido":"Tellechea",})

from django.shortcuts import render
import requests
from django.utils import timezone


def HomeView(request):
    hora_actual = timezone.now()

    year = hora_actual.year
    month = hora_actual.month
    day = hora_actual.day 

    date = f"{day}-{month}-{year}"

    hora = hora_actual.hour - 3
    minutos = hora_actual.minute
    segundos = hora_actual.second

    hora_restante = 23 - hora
    minutos_restante = 59 - minutos 
    segundos_restante = 59 - segundos

    print(hora, minutos, segundos)


    data = {
        'fecha': date,
        'horas_restantes': hora_restante,
        'minutos_restantes': minutos_restante,
        'segundos_restantes': segundos_restante,
        
    } 



    return render(request, 'index.html', {'data': data} )
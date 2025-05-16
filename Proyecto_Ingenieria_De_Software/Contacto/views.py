from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import os
import time
import smtplib
from datetime import datetime

# Create your views here.
def Contacto(request):

    nombre = request.POST.get('nombre')
    email = request.POST.get('email')
    celular = request.POST.get('celular')
    mensaje = request.POST.get('mensaje')

    if request.method == 'POST':

        #envia el correo---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        perrito = request.GET.get('nombre')

        message = 'El posible adoptante: ' + nombre + ' esta interesado en adoptar a: ' + perrito + '\n' + 'Se intereso en el porque: ' + mensaje + '\n' + 'Su numero de contacto es: ' + celular + '\n' + 'Su Email es: ' +email

        subject = 'Posible adoptante para ' + perrito

        message = 'Subject: {}\n\n{}'.format(subject, message)

        server = smtplib.SMTP('smtp.gmail.com', '587')

        server.starttls()

        server.login('fridaadopciones@gmail.com', 'formacion20040')

        server.sendmail('fridaadopciones@gmail.com', 'jorozco@proyectofrida.org.mx' , message)

        server.quit()
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        return render(request, 'Contactos/contacto.html',{'nombre':nombre,'email':email,'celular':celular,'mensaje':mensaje, 'perrito':perrito })

    return render(request, 'Contactos/contacto.html')
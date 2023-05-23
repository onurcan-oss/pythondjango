from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def kurslar(request):
    return HttpResponse('Kurs listesi')

def details(request):
    return HttpResponse('kurs detay sayfası')

def getCoursesByCategory(request, category):
    text = ""

    if(category == "programlama"):
        text = "Programlama kategorisine ait kurslar"
    elif (category == "web-gelistirme"):
        text = "web geliştirme kategorisine ait kurslar"
    else:
        text = "yanlış kategori seçimi"

    return HttpResponse(text)


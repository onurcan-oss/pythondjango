from django.db import models #kullanıcı modelini tanımladım.

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

#name surname ve telephone öğelerini dahil ettim ve uzunluğu max 100 ve 20 verdim.

# python manage.py makemigrations
#python manage.py migrate
#veritabanı geçişleri için bu komutları gerçeklerştirdim.
#ardından süper kullanıcı oluşturdum. python manage.py createsuperuser


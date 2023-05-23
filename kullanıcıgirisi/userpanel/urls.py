from django.urls import path
from . import views
from django.urls import include

app_name = 'userpanel'

urlpatterns = [
    path('', views.user_panel, name='user_panel'),
]


urlpatterns = [
    # Other URL patterns
    path('userpanel/', include('userpanel.urls', namespace='userpanel')),
]

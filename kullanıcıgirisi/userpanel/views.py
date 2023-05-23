from django.shortcuts import render

def user_panel(request):
    return render(request, 'userpanel/user_panel.html')

# Create your views here.

from django.shortcuts import render

# Create your views here.


def ind(request):
    return render(request ,'show.html')
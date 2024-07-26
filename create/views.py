from django.shortcuts import render

def create(req):
    return render(req, 'main/main.html')

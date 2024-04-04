from django.shortcuts import render

def index(request):
    context = {
        'prenom': "Paul",
        'age': 24
    }
    return render(request, "MonSite/templates/index.html", context=context)
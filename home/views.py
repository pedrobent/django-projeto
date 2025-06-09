from django.shortcuts import render

def home(request, *args, **kwargs):
    context = {
        'home': home,
    }

    return render(
        request,
        'home/home.html',
        context=context
    )

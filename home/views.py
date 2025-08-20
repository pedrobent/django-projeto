from django.shortcuts import render

def home(request, *args, **kwargs):
    context = {
        'home': home,
    }

    return render(
        request,
        'home/index.html',
        context=context
    )

def whatsapp(request, *args, **kwargs):
    context = {
        'whatsapp': whatsapp,
    }

    return render(
        request,
        'home/n8n.html',
        context=context
    )

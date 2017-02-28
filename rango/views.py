from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    #Return a rendered response to send to the client
    # We make use of the shortcut function to make out lives easier
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    msg0 = "Here is the about page. Tada!"
    msg1 = " This file has been composed by Andrew B. Kim"
    msg = msg0 + msg1
    context_dict = {'boldmessage': msg}
    return render(request, 'rango/about.html', context=context_dict)


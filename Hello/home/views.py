from lib2to3.fixes.fix_input import context

from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):

    context = {
        "variable": "Het Kothari"
    }
    # when we want to return simply a string, then we use HttpResponse
    # return HttpResponse("This is a Homepage")
    return render(request, 'index.html', context)


def about(request):
    return HttpResponse("This is a sample about page")


def services(request):
    return HttpResponse("This is a sample services page")


def contact(request):
    return HttpResponse("This is a sample contact page")
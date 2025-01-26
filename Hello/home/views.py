from lib2to3.fixes.fix_input import context
from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def index(request):

    # context = {
    #     "variable": "Het Kothari"
    # }
    # when we want to return simply a string, then we use HttpResponse
    # return HttpResponse("This is a Homepage")
    return render(request, 'index.html')
    # return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phno = request.POST.get("phno")
        desc = request.POST.get("desc")
        city = request.POST.get("city")
        zipcode = request.POST.get("zipcode")

        contact = Contact(name=name, email=email, phno=phno, desc=desc, city=city, zipcode=zipcode)
        contact.save()

    return render(request, 'contact.html')
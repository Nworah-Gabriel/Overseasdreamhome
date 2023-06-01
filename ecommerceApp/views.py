from django.shortcuts import render
from .models import Dream_Mansion, Cheap_Home
from .forms import Enquiry

# Create your views here.
def home(request):
    """
    A functional based view for the homepage
    """
    DreamMansion = Dream_Mansion.objects.all()
    CheapHomes = Cheap_Home.objects.all()

    return render(request, "index.html",
                  {
                    "DreamMansions":DreamMansion,
                    "CheapHomes": CheapHomes,
                   })


def CheapHomes(request):
    """
    A  functional based view for cheap homes
    """
    CheapHomes = Cheap_Home.objects.all()
    return render(request, "CheapHomes.html", {"CheapHomes": CheapHomes})


def DreamHomes(request):
    """
    A  functional based view for cheap homes
    """
    DreamHomes = Dream_Mansion.objects.all()
    return render(request, "DreamHomes.html", {"DreamHomes": DreamHomes})


def ContactUs(request):
    """
    A functional based view for the contact page
    """

    form = Enquiry(request.POST)

    if request.method == 'POST':
        print('posted')
        if form.is_valid():
            print('valid')
            form.save()
    return render(request, "ContactUs.html", {'form':form})
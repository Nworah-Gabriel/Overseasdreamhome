from django.shortcuts import render
from .models import Dream_Mansion, Cheap_Home, CheapHomeImage, DreamMansionImage
from .forms import Enquiry, Email

# Create your views here.
def home(request):
    """
    A functional based view for the homepage
    """
    
    DreamMansions = Dream_Mansion.objects.all()
    CheapHomes = Cheap_Home.objects.all()

    emailForm = Email(request.POST)

    if request.method == 'POST':
        print("posted")
        if emailForm.is_valid():
            print("valid")
            emailForm.save()
            

    return render(request, "index.html",
                  {
                    "DreamMansions":DreamMansions,
                    "CheapHomes": CheapHomes,
                    'emailForm':emailForm
                   })


def CheapHomes(request):
    """
    A  functional based view for cheap homes
    """
    CheapHomes = Cheap_Home.objects.all()

    emailForm = Email(request.POST)

    if request.method == 'POST':
        print("posted")
        if emailForm.is_valid():
            print("valid")
            emailForm.save()
            
    return render(request, "CheapHomes.html", {"CheapHomes": CheapHomes, 'emailForm':emailForm})


def DreamHomes(request):
    """
    A  functional based view for cheap homes
    """
    
    DreamHomes = Dream_Mansion.objects.all()

    emailForm = Email(request.POST)

    if request.method == 'POST':
        print("posted")
        if emailForm.is_valid():
            print("valid")
            emailForm.save()
            
    return render(request, "DreamHomes.html", {"DreamHomes": DreamHomes, 'emailForm':emailForm})


def ContactUs(request):
    """
    A functional based view for the contact page
    """

    form = Enquiry(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    emailForm = Email(request.POST)

    if request.method == 'POST':
        print("posted")
        if emailForm.is_valid():
            print("valid")
            emailForm.save()
            
    return render(request, "ContactUs.html", {'form':form, 'emailForm':emailForm})

def properties(request, id):
    mansion = ""
    images = ""
    print(id)
    form = Enquiry(request.POST)
    emailForm = Email(request.POST)

    if request.method == 'POST':
        print("posted")
        if emailForm.is_valid():
            print("valid")
            emailForm.save()

    if request.method == 'POST':
        print("posted")
        if form.is_valid():
            print("valid")
            form.save()

    try:
        DreamHomes = Dream_Mansion.objects.get(unique_id=id)
        Images = DreamMansionImage.objects.all()
        images = Images
        mansion = DreamHomes
    except:
        CheapHomes = Cheap_Home.objects.get(unique_id=id)
        Images = CheapHomeImage.objects.filter(CheapHomes__unique_id=id)
        images = Images
        mansion = CheapHomes
    # except:
       

    return render(request, "property.html", {"images":images, "mansion":mansion, 'form':form, 'emailForm':emailForm})
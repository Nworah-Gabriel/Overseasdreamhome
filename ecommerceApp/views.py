from django.shortcuts import render, HttpResponseRedirect
from .models import Dream_Mansion, Cheap_Home, CheapHomeImage, DreamMansionImage, CheapHomeFeature
from .models import CheapHomePropertie, DreamMansionFeature, DreamMansionPropertie
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
            return render(request, 'alert.html')

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
            return render(request, 'alert.html')
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
    Property = ""
    Features = ""
    print(id)
    form = Enquiry(request.POST)
    emailForm = Email(request.POST)

    if request.method == 'POST':
        print("posted")
        if emailForm.is_valid():
            print("valid")
            emailForm.save()
        # return render(request, 'alert.html')

    if request.method == 'POST':
        print("posted")
        if form.is_valid():
            print("valid")
            form.save()
        return render(request, 'propertyAlert.html', {'id':id})
    try:
        DreamHomes = Dream_Mansion.objects.get(unique_id=id)
        Images = DreamMansionImage.objects.filter(DreamMansion__unique_id=id)
        property = DreamMansionPropertie.objects.filter(DreamMansion__unique_id=id)
        features = DreamMansionFeature.objects.filter(DreamMansion__unique_id=id)
        images = Images
        mansion = DreamHomes
        Property = property
    except:
        CheapHomes = Cheap_Home.objects.get(unique_id=id)
        Images = CheapHomeImage.objects.filter(CheapHomes__unique_id=id)
        property = CheapHomePropertie.objects.filter(CheapHomes__unique_id=id)
        features = CheapHomeFeature.objects.filter(CheapHomes__unique_id=id)
        images = Images
        mansion = CheapHomes
        Property = property
       

    return render(request, "property.html",
                  {"images":images,
                   "mansion":mansion,
                   'form':form,
                   'emailForm':emailForm,
                   'properties':Property,
                   'features':features})

def about(request):
    """
    A functional based view for the about page
    """

    emailForm = Email(request.POST)

    if request.method == 'POST':
        print("posted")
        if emailForm.is_valid():
            print("valid")
            emailForm.save()
        # return render(request, 'alert.html')
    return render(request, 'AboutUs.html', {'emailForm':emailForm})
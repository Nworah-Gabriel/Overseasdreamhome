from django.db import models
from datetime import datetime
from uuid import uuid4


DESCRIPTION = """
Write an organized description of the asset to be displayed. eg

This five bedroom villa for sale in São Brás de Alportel is just one kilometre from the town centre where there are supermarkets, restaurants, cafes, schools and other shops. Currently listed as a five bedroom property due to the extra annexes adjacent to the main house.

The main house consists of a formal dining area with a traditional fireplace, a fully fitted kitchen, a good size pantry, lounge with another fireplace, a mezzanine style office, three bedrooms, one large family bathroom and a conservatory with a BBQ installed, sink and seating area. 

There is a further large bedroom, currently being used as a storage room, and a bathroom in one of the annexes with the second annex comprising the fifth bedroom, however, both annexes do need refurbishing.

Additional features include: two entrances to the property, a fountain, solid wood carpentry in the wardrobes, front gate on the road, cobblestone driveway, solar panels for water, double glazed windows and this property is sold furnished but is negotiable. 

 São Bras is a popular town amongst people that relocate to the Algarve as it has friendly locals and a slower pace of life. In an elevated position north of Faro, the whole area offers lovely views down towards the sea.  - REF: IDH32943
"""



# Create your models here.
class Enquirie(models.Model):
    """
    A model class that stores inquiry informations from clients
    """

    FirstName = models.CharField(max_length=50, verbose_name="First Name")
    LastName = models.CharField(max_length=50, verbose_name="First Name")
    Mobile_No = models.CharField(max_length=20, verbose_name="Mobile No")
    Email = models.CharField(max_length=200)
    Subject = models.CharField(max_length=400, default="Property Enquiry")
    Message = models.TextField()

    def __str__(self):
        return self.Message

class Emails(models.Model):
    """
    A model class for storing emails
    """
    Email = models.CharField(max_length=200)
    DatePub = models.DateTimeField(default=datetime.now(), verbose_name="Date Created")

    def __str__(self):
        return self.Email


class Cheap_Home(models.Model):
    """
    A model class for storing cheap home data
    """

    Title = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    DollarsPrice = models.CharField(max_length=50, default="$50,000", verbose_name="Dollar Price")
    EurosPrice = models.CharField(max_length=50, default="€20,000", verbose_name="Euros Price")
    PoundsPrice = models.CharField(max_length=50, default="£35,000", verbose_name="Pounds Price")
    CoverImageUrl = models.CharField(max_length=2000, verbose_name="Cover Image Url")
    DatePub = models.DateTimeField(default=datetime.now(), verbose_name="Date Created", editable=False)
    unique_id = models.UUIDField(default=uuid4, editable=False, unique=True)
    Description = models.TextField(default=DESCRIPTION)


    def __str__(self):
        return self.Title
    

class Dream_Mansion(models.Model):
    """
    A model class for storing dream mansion data
    """

    Title = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    DollarsPrice = models.CharField(max_length=50, default="$50,000")
    EurosPrice = models.CharField(max_length=50, default="€20,000")
    PoundsPrice = models.CharField(max_length=50, default="£35,000")
    CoverImageUrl = models.CharField(max_length=2000, verbose_name="Cover Image Url")
    DatePub = models.DateTimeField(default=datetime.now(), verbose_name="Date Created", editable=False)
    unique_id = models.UUIDField(default=uuid4, editable=False, unique=True)
    Description = models.TextField(default=DESCRIPTION)

    def __str__(self):
        return self.Title
    

class DreamMansionImage(models.Model):
    """
    A model class for storing image url linked to a property
    """

    DreamMansion = models.ForeignKey(to="Dream_Mansion", on_delete=models.CASCADE)
    Created = models.DateTimeField(default=datetime.now())
    ImageUrl = models.CharField(max_length=2000)
    unique_id = models.UUIDField(default=uuid4, editable=False, unique=True)

    def __str__(self):
        return self.DreamMansion.Title
    

class DreamMansionPropertie(models.Model):
    """
    A model class for storing image url linked to a property
    """

    DreamMansion = models.ForeignKey(to="Dream_Mansion", on_delete=models.CASCADE)
    Created = models.DateTimeField(default=datetime.now)
    Name = models.CharField(max_length=50, default="Plot size")
    Value = models.CharField(max_length=50, default="1200 m2")
    unique_id = models.UUIDField(default=uuid4, editable=False, unique=True)

    def __str__(self):
        return self.DreamMansion.Title


class DreamMansionFeature(models.Model):
    """
    A model class for storing image url linked to a property
    """

    DreamMansion = models.ForeignKey(to="Dream_Mansion", on_delete=models.CASCADE)
    Created = models.DateTimeField(default=datetime.now)
    Feature = models.CharField(max_length=50, default="Garden")
    unique_id = models.UUIDField(default=uuid4, editable=False, unique=True)

    def __str__(self):
        return self.DreamMansion.Title

class CheapHomeImage(models.Model):
    """
    A model class for storing image url linked to a property
    """

    CheapHomes = models.ForeignKey(to="Cheap_Home", on_delete=models.CASCADE)
    Created = models.DateTimeField(default=datetime.now())
    ImageUrl = models.CharField(max_length=2000)
    unique_id = models.UUIDField(default=uuid4, editable=False, unique=True)

    def __str__(self):
        return self.CheapHomes.Title
    

class CheapHomePropertie(models.Model):
    """
    A model class for storing image url linked to a property
    """

    CheapHomes = models.ForeignKey(to="Cheap_Home", on_delete=models.CASCADE)
    Created = models.DateTimeField(default=datetime.now)
    Name = models.CharField(max_length=50, default="Plot size")
    Value = models.CharField(max_length=50, default="1200 m2")
    unique_id = models.UUIDField(default=uuid4, editable=False, unique=True)

    def __str__(self):
        return self.DreamMansion.Title


class CheapHomeFeature(models.Model):
    """

    A model class for storing image url linked to a property
    """

    CheapHomes = models.ForeignKey(to="Cheap_Home", on_delete=models.CASCADE)
    Created = models.DateTimeField(default=datetime.now)
    Feature = models.CharField(max_length=50, default="Garden")
    unique_id = models.UUIDField(default=uuid4, editable=False, unique=True)

    def __str__(self):
        return self.DreamMansion.Title
from django.db import models
from datetime import datetime
from uuid import uuid4


DESCRIPTION = """

        This comfortable 2-bedroom bungalow with roof terrace is situated in a quiet location and has a shared swimming pool.
        
        The house comprises an open plan fully fitted kitchen/dining/living area, two bedrooms and two bathrooms.
        
        The living room has patio doors opening onto a paved terrace covered by a retractable awning.
        
        There is stone paving right round the house and gravelled areas for low-maintenance gardening.
        
        External steps lead up to the large, tiled roof terrace, from which vantage point stunning views are afforded over serene countryside and olive groves to the majestic White Mountain range.
        
        Being only 7km from the white, sandy beaches of Almirida, this makes the perfect holiday home for those wanting peace and quiet, but who also want to be close enough to the larger villages of Almirida or Kalives with their white, sandy beaches and all shopping amenities, post office, banks, supermarkets, tavernas, restaurants & coffee shops.
        
        The traditional village of Drapanos has a well-stocked mini-market and a few tavernas with delicious Cretan cuisine.
        
        BENEFITS:
        
        Air Conditioning
        Solar Panel
        Plumbing for Central Heating
        Aluminium Windows & Doors with Double Glazing & Security Shutters
        Storage Area
        Garden
        Shared Swimming Pool
        BBQ
        Roof Terrace
        Pergola
        All White Goods Included
        Fully Furnished
        Quiet Area
        Country & Mountain Views
        Within Walking Distance to Village Square and Local Amenities
        Short Drive to the Beach & further Amenities

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
    

class Cheap_Home(models.Model):
    """
    A model class for storing cheap home data
    """

    Title = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Price = models.CharField(max_length=200)
    CoverImageUrl = models.CharField(max_length=2000, verbose_name="Cover Image Url")
    DatePub = models.DateTimeField(default=datetime.now(), verbose_name="Date Created", editable=False)
    unique_id = models.UUIDField(default=uuid4(), editable=False)
    Description = models.TextField(default=DESCRIPTION)


    def __str__(self):
        return self.Title
    

class Dream_Mansion(models.Model):
    """
    A model class for storing dream mansion data
    """

    Title = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Price = models.CharField(max_length=200)
    CoverImageUrl = models.CharField(max_length=2000, verbose_name="Cover Image Url")
    DatePub = models.DateTimeField(default=datetime.now(), verbose_name="Date Created", editable=False)
    unique_id = models.UUIDField(default=uuid4(), editable=False)
    Description = models.TextField(default=DESCRIPTION)

    def __str__(self):
        return self.Title
    

class DreamMansionImages(models.Model):
    """
    A model class for storing image url linked to a property
    """

    DreamMansion = models.ForeignKey(to="Dream_Mansion", on_delete=models.CASCADE)
    Created = models.DateTimeField(default=datetime.now())
    ImageUrl = models.CharField(max_length=2000)
    unique_id = models.UUIDField(default=uuid4, editable=False)

    def __str__(self):
        return self.DreamMansion.Title
    
class CheapHomeImages(models.Model):
    """
    A model class for storing image url linked to a property
    """

    CheapHomes = models.ForeignKey(to="Cheap_Home", on_delete=models.CASCADE)
    Created = models.DateTimeField(default=datetime.now())
    ImageUrl = models.CharField(max_length=2000)
    unique_id = models.UUIDField(default=uuid4, editable=False)

    def __str__(self):
        return self.CheapHomes.Title
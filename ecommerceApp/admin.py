from django.contrib import admin
from .models import Dream_Mansion, Cheap_Home, Enquirie, DreamMansionImage, CheapHomeImage, Emails
from .models import DreamMansionFeature, DreamMansionPropertie, CheapHomeFeature, CheapHomePropertie

# Register your models here.
admin.site.register(Dream_Mansion)
admin.site.register(Cheap_Home)
admin.site.register(Enquirie)
admin.site.register(DreamMansionImage)
admin.site.register(CheapHomeImage)
admin.site.register(Emails)
admin.site.register(CheapHomePropertie)
admin.site.register(CheapHomeFeature)
admin.site.register(DreamMansionFeature)
admin.site.register(DreamMansionPropertie)

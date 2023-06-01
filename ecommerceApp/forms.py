from django import forms
from .models import Enquirie

class Enquiry(forms.ModelForm):
    """
    A model form for storing equiry data
    """

    class Meta:
        model = Enquirie
        fields = ['FirstName', 'LastName', 'Mobile_No', 'Email', 'Message', 'Subject']
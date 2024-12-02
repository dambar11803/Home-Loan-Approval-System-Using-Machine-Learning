from django import forms  
from .models import ClientDetails 
from django.core.exceptions import ValidationError



    

class ClientDetailsForm(forms.ModelForm):
       
    class Meta:
        model = ClientDetails 
        fields = '__all__'
        
        
        
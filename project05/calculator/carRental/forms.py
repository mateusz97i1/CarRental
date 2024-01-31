from django import forms
from .models import RentCarModel,CarModel,FaqModel,RateUSModel
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type='date'

class RentForm(ModelForm):
    class Meta:
        model=RentCarModel
        fields="__all__"

        labels = {
            'fullName': 'Full Name',
            'country': 'Country',
            'idNumber': 'ID Number',
            'phone': 'Phone',
            'email': 'Email',
            'carBrand': 'Car Brand',
            'fromDate': 'From Date',
            'toDaate': 'To Date',
            'otheText': 'Other Text',
        }

        label_suffix = ''
        

        widgets = {
        'fullName': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
        'country': forms.TextInput(attrs={'placeholder': 'Enter your country'}),
        'idNumber': forms.TextInput(attrs={'placeholder': 'Enter your ID number'}),
        'phone': forms.NumberInput(attrs={'placeholder': 'Enter your phone number'}),
        'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        'fromDate': DateInput(),
        'toDaate': DateInput(),
        'otheText': forms.Textarea(attrs={'placeholder': 'Any other request'}),
        
    }


class CarForm(ModelForm):
    class Meta:
        model=CarModel
        fields="__all__"



class FaqForm(ModelForm):
    class Meta:
        model=FaqModel
        fields='__all__'

        label_suffix = ' '

        widgets = {
                    
                    'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
               
                    
                }
        
        labels = {
        'text': '',
        'email': '',
    
    }
        
class RateUSForm(ModelForm):


    RATING_CHOICES = [
        ('★★★★★', '★★★★★'),
    ('★★★★', '★★★★'),
    ('★★★', '★★★'),
    ('★★', '★★'),
    ('★', '★'),
    ]

    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.Select(attrs={'onchange': 'updateRatingDisplay()'}),required=False)
    



    class Meta:
        model=RateUSModel
        exclude=['date']
        fields="__all__"


        label_suffix = ' '


        widgets = {
                    'nick': forms.TextInput(attrs={'placeholder': 'Enter your name'}),

                    
                }
        
        labels = {
        'text': '',
        'nick': '',
        'rating': '',
        
    
    }
        

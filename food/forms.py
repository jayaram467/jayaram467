
from django import forms
from django.contrib.auth.models import User
from . import models
from .models import cust, ordernow

from django.forms import ModelForm


class CustomerUserForm(ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        widgets = {
        'password': forms.PasswordInput()
        }



        
class CustomerForm(ModelForm):
    class Meta:
        model=models.cust
        fields=['pincode','address','mobile','state','country','gender']

class ContactusForm(ModelForm):
  
    model = models.contactus
    fields =['name','email','phone','message']


class OrdernowForm(forms.Form):
    class Meta:
        Model = ordernow


    fields =['first_name','last_name','adress','email']
    FOOD_CHOICES = [
        ('MEALS','MEALS'),
        ('CHICKEN BIRAYANI','CHICKEN BIRAYANI'),
        ('MUTTON BIRAYANI','MUTTON BIRAYANI'),
        ('CHICKEN FRIEDRICE','CHICKEN FRIEDRICE'),
        ('PIZZA','PIZZA'),
        ('CHICKEN PIZZA','CHICKEN PIZZA'),
        ('VEG PIZZA','VEG PIZZA'),
        ('BURGER','BURGER'),
    ]
    FOOD_PRICES =[
        ('MEALS',120),
        ('CHICKEN BIRAYANI',180),
        ('MUTTON BIRAYANI',250),
        ('CHICKEN FRIEDRICE',160),
        ('PIZZA',240),
        ('CHICKEN PIZZA',280),
        ('VEG PIZZA',210),
        ('BURGER',120),

    ]
    CHOICES = (
        ('MEALS', (
            ('120', '120'),
        )),
        ('CHICKEN BIRAYANI', (
            ('180', '180'),
        )),
        ('MUTTON BIRAYANI', (
            ('250', '250'),
        )),
        ('CHICKEN FRIEDRICE',(
            ('160 ','160'),
          
        )),
        ('PIZZA',(
            ('240','240'),
        )),
        ('CHICKEN PIZZA',(
            ('280','280'),
         
        )),
        ('VEG PIZZA',(
            ('210','210'),
        
        )),
        ('BURGER',(
            ('120','120'),
        ))
    )
    ITEMPRICE_CHOICES=(('120','MEALS '),('180','CHICKEN BIRAYANI'),('250  ','MUTTON BIRAYANI'),
    ('160','CHICKEN FRIEDRICE'),('240','PIZZA'),('280 ','CHICKEN PIZZA'),
    ('210','VEG PIZZA'),('120','BURGER'))
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email =  forms.EmailField()
    adress = forms.CharField(max_length=200)
    fooditem = forms.CharField(label='select the item',widget=forms.Select(choices=FOOD_CHOICES))
    foodprices = forms.CharField(widget=forms.Select(choices=CHOICES))
    

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['fooditem'].queryset = ordernow.objects.none()
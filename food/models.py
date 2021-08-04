from django.db import models
from django.contrib.auth.models import User


class food(models.Model):
    food=models.CharField(max_length=100)


class cust(models.Model):
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (FeMale, 'Female'),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    state = models.CharField(max_length=40,null=False)
    country = models.CharField(max_length=40)
    pincode = models.CharField(max_length=20,null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,
                              default=Male)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class contactus(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.BigIntegerField()
    message = models.CharField(max_length=200)

class ordernow(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email =  models.EmailField()
    adress = models.CharField(max_length=200)
    # FOOD_CHOICES = [
    #     ('MEALS','MEALS'),
    #     ('CHICKEN BIRAYANI','CHICKEN BIRAYANI'),
    #     ('MUTTON BIRAYANI','MUTTON BIRAYANI'),
    #     ('CHICKEN FRIEDRICE','CHICKEN FRIEDRICE'),
    #     ('PIZZA','PIZZA'),
    #     ('CHICKEN PIZZA','CHICKEN PIZZA'),
    #     ('VEG PIZZA','VEG PIZZA'),
    #     ('BURGER','BURGER'),
    # ]
    # FOOD_PRICES =[
    #     ('MEALS',120),
    #     ('CHICKEN BIRAYANI',180),
    #     ('MUTTON BIRAYANI',250),
    #     ('CHICKEN FRIEDRICE',160),
    #     ('PIZZA',240),
    #     ('CHICKEN PIZZA',280),
    #     ('VEG PIZZA',210),
    #     ('BURGER',120),

    # ]
    # CHOICES = (
    #     ('MEALS', (
    #         ('120', '120'),
    #     )),
    #     ('CHICKEN BIRAYANI', (
    #         ('180', '180'),
    #     )),
    #     ('MUTTON BIRAYANI', (
    #         ('250', '250'),
    #     )),
    #     ('CHICKEN FRIEDRICE',(
    #         ('160 ','160'),
          
    #     )),
    #     ('PIZZA',(
    #         ('240','240'),
    #     )),
    #     ('CHICKEN PIZZA',(
    #         ('280','280'),
         
    #     )),
    #     ('VEG PIZZA',(
    #         ('210','210'),
        
    #     )
    #     ('BURGER',(
    #         ('120','120'),
    #     ))
    # ),
    # # ITEMPRICE_CHOICES=(('120','MEALS '),('180','CHICKEN BIRAYANI'),('250','MUTTON BIRAYANI'),
    # # ('160','CHICKEN FRIEDRICE'),('240','PIZZA'),('280 ','CHICKEN PIZZA'),
    # # ('210','VEG PIZZA'),('120','BURGER')),

    # # fooditem = models.CharField(max_length=100,choices= FOOD_CHOICES,default=None),
    # # amount = models.CharField(max_length=100,choices=CHOICES,default=None)

    





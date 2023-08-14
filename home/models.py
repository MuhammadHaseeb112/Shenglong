from django.db import models


class product(models.Model): 
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    new = models.BooleanField(default= False)
    manafacture = models.CharField(max_length=100)
    location = models.CharField(max_length=60)
    price = models.IntegerField()
    discription = models.TextField()
    img = models.ImageField(upload_to='images/')
    img2 = models.ImageField(upload_to='images/',null=True,blank=True)
    img3 = models.ImageField(upload_to='images/',null=True,blank=True)
    img4 = models.ImageField(upload_to='images/',null=True,blank=True)
    img5 = models.ImageField(upload_to='images/',null=True,blank=True)
    img6 = models.ImageField(upload_to='images/',null=True,blank=True)
    img7 = models.ImageField(upload_to='images/',null=True,blank=True)
    img8 = models.ImageField(upload_to='images/',null=True,blank=True)
    img9 = models.ImageField(upload_to='images/',null=True,blank=True)
    img10 = models.ImageField(upload_to='images/',null=True,blank=True)
    catagory = models.CharField(max_length=100)
    disable = models.BooleanField(default= False)


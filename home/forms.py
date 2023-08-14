from django import forms
from .models import *


class productForm(forms.ModelForm):

	class Meta:
		model = product
		fields = ['name','model','new','manafacture','location','price','discription','img','img2','img3','img4','img5','img6','img7','img8','img9','img10','catagory']

class disable_productForm(forms.ModelForm):

	class Meta:
		model = product
		fields = ['disable']


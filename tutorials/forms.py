# forms.py
from django import forms
from .models import *

class HotelForm(forms.ModelForm):

	class Meta:
		model = Upload
		fields = ['name', 'hotel_Main_Img']
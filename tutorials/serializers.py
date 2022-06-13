from rest_framework import serializers 
from tutorials.models import Tutorial,Hotel,Register
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('name', 'hotel_Main_Img')
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('username','password','email','phone','ucode')
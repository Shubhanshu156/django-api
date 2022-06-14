from rest_framework import serializers 
from tutorials.models import response,Register, Upload
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = response
        fields = ('username','description','brand','coordinate1','coordinate2','object_size_height','object_size_width','ref_object_size_height','ref_object_size_width','is_verify')
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ('id','username', 'image','description','brand','coordinate1','coordinate2','ref_object_size_height','ref_object_size_width','is_verify')
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('id','createddate','lastdate','is_active','is_approved','username','password','email','phone','ucode','region','category','created_by','updated_by')
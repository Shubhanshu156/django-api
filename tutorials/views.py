import datetime,jwt
from unicodedata import category
import json
from django.forms import model_to_dict
from django.conf import Settings
from turtle import width
from collections import OrderedDict

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from prometheus_client import REGISTRY
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
import cv2
from  tutorials.object_detector import *
import numpy as np
from tutorials.forms import HotelForm
from rest_framework.exceptions import ParseError
from tutorials.models import  Register, response, Upload
from tutorials.serializers import TutorialSerializer,ImageSerializer,RegisterSerializer
from rest_framework.decorators import api_view
# import ListAPIView 








def get_object_size(path):
    
# Load Aruco detector
    parameters = cv2.aruco.DetectorParameters_create()
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
    # Load Object Detector
    detector = HomogeneousBgDetector()

    # Load Image
    path="tutorials"+path
    img = cv2.imread(path)

    # find the aruco markers in the image

    # print(type(img))
    # Get Aruco marker
    corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)

    # Draw polygon around the marker
    int_corners = np.int0(corners)
    cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

    # Aruco Perimeter
    aruco_perimeter = cv2.arcLength(corners[0], True)

    # Pixel to cm ratio
    # 20 as perimeter of refernce is 20



    pixel_cm_ratio = aruco_perimeter / 20

    contours = detector.detect_objects(img)

    # Draw objects boundaries
    for cnt in contours:
        # Get rect
        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect

        # Get Width and Height of the Objects by applying the Ratio pixel to cm
        object_width = w / pixel_cm_ratio
        object_height = h / pixel_cm_ratio
        # Display rectangle
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        if object_width > 5:
            cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
            cv2.polylines(img, [box], True, (255, 0, 0), 2)
            cv2.putText(img, "Width {} cm".format(round(object_width, 1)), (int(
                x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            cv2.putText(img, "Height {} cm".format(round(object_height, 1)), (int(
                x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)

    return object_height,object_width
    # cv2.imwrite('result.jpg', img)
    # cv2.imshow("Image", img)
    # cv2.imwrite('result2.jpg', img)  
    # cv2.waitKey(0)





# to create a new user
@api_view(['POST'])
def user(request):
    if request.method == 'POST':
        try:
           
            if Register.objects.filter(username=request.data['username']).exists():
                return Response({"message":"username already exists"},status=status.HTTP_400_BAD_REQUEST)
            
            a=RegisterSerializer(data=request.data)
            if a.is_valid():
                    product=Register.objects.create(
                username=request.data['username'],
                password=request.data['password']
                ,email=request.data['email'],
                phone=request.data['phone'],
                ucode=request.data['ucode'],
                fullname=request.data['fullname'],
                category=request.data['category'],
                region=request.data['region'],
                )
                    id1=product.id
                    val=Register.objects.get(id=id1)
                    val.created_by=id1
                    val.updated_by=id1
                    val.save()
                    a=Register.objects.all()
                    a=a.filter(id=product.id)
                    print("value of a is",a)
                    print(a[0])
                    a=RegisterSerializer(a,many=True)
                    return JsonResponse(a.data, safe=False)
   
            else:
                print("it is not a valid detail register serializer")
                return Response({"message":"invalid details"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

            print(request.data)
            data = JSONParser().parse(request)
            # print(data)
            register_serilizer = RegisterSerializer(data=request.data)
            # print(register_serilizer)
            if register_serilizer.is_valid():
                register_serilizer.save()

                # print(data['username'])/
                # token = Token.objects.create(user=data['username'])
            
                return JsonResponse(register_serilizer.data, status=status.HTTP_201_CREATED) 
            else:
                print("you entered somthing wrong")






# to login user and generate a token for 15 days 

@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    try:
        username = request.data['username']
        password = request.data['password']
        user = Register.objects.filter(username=username,password=password).first()
        user.save()
        if user is None:
            raise AuthenticationFailed('User not found!')

        payload = {
            'id': user.id,
            'fullname': user.fullname,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=21660),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response
    except:
        raise AuthenticationFailed('User not found!')








# to upload image


@api_view(['post'])
def upload_docs(request):
    
    token=request.COOKIES.get('jwt')
    # token="abc"
    if not token:
        raise AuthenticationFailed("Authentication Failed")
    try:
        payload=jwt.decode(token,'secret',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Token Expired")
    try:
        file = request.data['image']
        username=request.data['username']
        brand=request.data['brand']
        description=request.data['description']
        coordinate1=request.data['coordinate1']
        coordinate2=request.data['coordinate2']
        height=request.data['ref_object_height']
        width=request.data['ref_object_width']
    
    except KeyError:
       
        raise ParseError('Some Fields are missing')
    try:
        product = Upload.objects.create(username=username, image=file,brand=brand,description=description,coordinate1=coordinate1,coordinate2=coordinate2,ref_object_size_height=height,ref_object_size_width=width)
        product.save()
        print("value of product is",product)   
        print(product.id)
        a=Upload.objects.all()
        a=a.filter(id=product.id)
        print(a)
        a=ImageSerializer(a,many=True)
        
        return JsonResponse(a.data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)










# to get size of object from image id


@api_view(['GET'])
def get_size(request,id):
    # tutorials = response.objects.filter(title=title)
    token=request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed("Authentication Failed")
    try:
        payload=jwt.decode(token,'secret',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Token Expired")
    if request.method == 'GET': 
        # try:
        try:
                a=Upload.objects.all()
                a=a.filter(id=id)
                a=ImageSerializer(a,many=True)
                path=a.data[0]['image']
                height,width=get_object_size(path)
                print(path)
            # tutorials_serializer = TutorialSerializer(tutorials, many=True)
                d="height="+str(height)+" width="+str(width)
                a=response.objects.create(
                    username=a.data[0]['username'],
                
                brand=a.data[0]['brand'],
                description=a.data[0]['description'],coordinate1=a.data[0]['coordinate1'],coordinate2=a.data[0]['coordinate2'],ref_object_size_height=a.data[0]['ref_object_size_height'],ref_object_size_width=a.data[0]['ref_object_size_width'],object_size_height=height,object_size_width=width,
                is_verify=a.data[0]['is_verify'])
                dict_obj=model_to_dict(a)
                serail=json.dumps(dict_obj)
                # a=TutorialSerializer(a,many=True)
                return HttpResponse(serail, content_type='application/json')
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
        # except:
            return JsonResponse({'message': 'Please Enter Correct Image Name'})
        # return JsonResponse(tutorials_serializer.data, safe=False)
@api_view(['GET'])
def getall(request):
    try:
        a=Upload.objects.all()
        a=ImageSerializer(a,many=True)
        return JsonResponse(a.data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)




@permission_classes((AllowAny,))
@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    token=request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed("Authentication Failed")
    try:
        payload=jwt.decode(token,'secret',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Token Expired")
    if request.method == 'GET':
        tutorials = response.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = response.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 






        
 






@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        print("geeting image with id so process your image here")
        tutorial = response.objects.get(pk=pk) 
    except response.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'response was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    



        
@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = response.objects.filter(published=True)
        
    if request.method == 'GET': 
     
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    
def hotel_image_view(request):
  
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'hotel_image_form.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')
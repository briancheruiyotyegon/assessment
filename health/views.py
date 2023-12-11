from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser, Category, Data
from .serializers import CustomUserSerializer, CategorySerializer, DataSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    method='get',
    operation_description='Get all users',
    responses={200: CustomUserSerializer(many=True)}
)
@api_view(['GET'])
def get_users(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    method='get',
    operation_description='Get a user by ID',
    responses={200: CustomUserSerializer()}
)
@api_view(['GET'])
def get_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    serializer = CustomUserSerializer(user, many=False)
    return Response(serializer.data)
@swagger_auto_schema(
    method='get',
    operation_description='Get a user by username',
    responses={200: CustomUserSerializer()}
)
@api_view(['GET'])
def search_user_by_username(request,username):
    user=CustomUser.objects.filter(username=username)
    serializer=CustomUserSerializer(user,many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    method='post',
    operation_description='Create a new user',
    request_body=CustomUserSerializer,
    responses={200: CustomUserSerializer()}
)
@api_view(['POST'])
def create_user(request):
    serializer = CustomUserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@swagger_auto_schema(
    method='put',
    operation_description='Update a user by ID',
    request_body=CustomUserSerializer,
    responses={200: CustomUserSerializer()}
)
@api_view(['PUT'])
def update_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    serializer = CustomUserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@swagger_auto_schema(
    method='delete',
    operation_description='Delete a user by ID',
    responses={200: 'User deleted successfully'}
)
@api_view(['DELETE'])
def delete_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.delete()
    return Response("User deleted successfully")

@swagger_auto_schema(
    method='get',
    operation_description='categories',
    responses={200: CategorySerializer(many=True)}
)
@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
@swagger_auto_schema(
    method='get',
    operation_description='Get a category by ID',
    responses={200: CategorySerializer()}
)
@api_view(['GET'])
def get_category(request, category_id):
    category = Category.objects.get(id=category_id)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)
@swagger_auto_schema(
    method='get',
    operation_description='Get a category by name',
    responses={200: CategorySerializer()}
)
@api_view(['GET'])
def search_category_by_name(request,name):
    category=Category.objects.filter(name=name)
    serializer=CategorySerializer(category,many=True)
    return Response(serializer.data)
@swagger_auto_schema(
    method='post',
    operation_description='Create a new category',
    request_body=CategorySerializer,
    responses={200: CategorySerializer()}
)
@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@swagger_auto_schema(
    method='put',
    operation_description='Update a category by ID',
    request_body=CategorySerializer,
    responses={200: CategorySerializer()}
)
@api_view(['PUT'])
def update_category(request, category_id):
    category = Category.objects.get(id=category_id)
    serializer = CategorySerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@swagger_auto_schema(
    method='delete',
    operation_description='Delete a category by ID',
    responses={200: 'Category deleted successfully'}
)
@api_view(['DELETE'])
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return Response("Category deleted successfully")
@swagger_auto_schema(
    method='get',
    operation_description='data',
    responses={200: DataSerializer(many=True)}
)
@api_view(['GET'])
def get_datas(request):
    datas = Data.objects.all()
    serializer = DataSerializer(datas, many=True)
    return Response(serializer.data)
@swagger_auto_schema(
    method='get',
    operation_description='Get a data by ID',
    responses={200: DataSerializer()}
)
@api_view(['GET'])
def get_data(request, data_id):
    data = Data.objects.get(id=data_id)
    serializer = DataSerializer(data, many=False)
    return Response(serializer.data)
@swagger_auto_schema(
    method='post',
    operation_description='Create a new data',
    request_body=DataSerializer,
    responses={200: DataSerializer()}
)
@api_view(['POST'])
def create_data(request):
    serializer = DataSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@swagger_auto_schema(
    method='put',
    operation_description='Update a data by ID',
    request_body=DataSerializer,
    responses={200: DataSerializer()}
)
@api_view(['PUT'])
def update_data(request, data_id):
    data = Data.objects.get(id=data_id)
    serializer = DataSerializer(instance=data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@swagger_auto_schema(
    method='delete',
    operation_description='Delete a data by ID',
    responses={200: 'Data deleted successfully'}
)
@api_view(['DELETE'])
def delete_data(request, data_id):
    data = Data.objects.get(id=data_id)
    data.delete()
    return Response("Data deleted successfully")

@swagger_auto_schema(
    method='get',
    operation_description='Get a data by Institution Name',
    responses={200: DataSerializer()}
)
@api_view(['GET'])
def search_data_by_institution_name(request,institution_name):
    data=Data.objects.filter(institution_name=institution_name)
    serializer=DataSerializer(data,many=True)
    return Response(serializer.data)
@swagger_auto_schema(
    method='get',
    operation_description='Get a data by Event Name',
    responses={200: DataSerializer()}
)
@api_view(['GET'])
def search_data_by_eventName(request,eventName):
    data=Data.objects.filter(eventName=eventName)
    serializer=DataSerializer(data,many=True)
    return Response(serializer.data)
@swagger_auto_schema(
    method='get',
    operation_description='Get a data by event Location',
    responses={200: DataSerializer()}
)
@api_view(['GET'])
def search_data_by_eventLocation(request,eventLocation):
    data=Data.objects.filter(eventLocation=eventLocation)
    serializer=DataSerializer(data,many=True)
    return Response(serializer.data)
@swagger_auto_schema(
    method='get',
    operation_description='Get a data first name',
    responses={200: DataSerializer()}
)
@api_view(['GET'])
def search_data_by_first_name(request,first_name):
    data=Data.objects.filter(first_name=first_name)
    serializer=DataSerializer(data,many=True)
    return Response(serializer.data)
@swagger_auto_schema(
    method='get',
    operation_description='Get a data by event Date',
    responses={200: DataSerializer()}
)
@api_view(['GET'])
def search_data_by_eventDate(request,eventDate):
    data=Data.objects.filter(eventDate=eventDate)
    serializer=DataSerializer(data,many=True)
    return Response(serializer.data)


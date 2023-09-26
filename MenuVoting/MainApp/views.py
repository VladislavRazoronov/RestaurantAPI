from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from MainApp.serializers import *
from MainApp import models
from rest_framework.decorators import api_view
from datetime import datetime


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET', 'POST'])
def restaurant_list(request, format=None):
    """
    List all restaurants or create new restaurant.
    """
    if request.method == 'GET':
        restaurants = models.Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def restaurant_detail(request, pk, format=None):
    """
    Retrieve, update or delete a restaurant.
    """
    try:
        restaurant = models.Restaurant.objects.get(pk=pk)
    except models.Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def menu_list(request, format=None):
    """
    List all menus or create new menu.
    """
    if request.method == 'GET':
        menus = models.Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def menu_detail(request, pk, format=None):
    """
    Retrieve, update or delete a menu.
    """
    try:
        menu = models.Menu.objects.get(pk=pk)
    except models.Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MenuSerializer(menu)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def employee_list(request, format=None):
    """
    List all employees or create new employee.
    """
    if request.method == 'GET':
        menus = models.employee.objects.all()
        serializer = EmployeeSerializer(menus, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk, format=None):
    """
    Retrieve, update or delete an employee.
    """
    try:
        employee = models.employee.objects.get(pk=pk)
    except models.employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT'])   
def getDailyMenus(request, format=None):
    day = datetime.now().strftime('%A')
    if request.method == 'GET':
        try:
            menus =  models.Menu.objects.filter(day=day).all()
            serializer = MenuSerializer(menus, many=True)
            return Response(serializer.data)
        except models.Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        data = request.data
        try:
            employee = models.employee.objects.get(email=data["employee_email"])
            restaurant = models.Restaurant.objects.get(name=data["restaurant"])
            if(employee.selectedMenu != None):
                oldMenu = models.Menu.objects.get(employee.selectedMenu)
                if(oldMenu.votes > 1):
                    oldMenu.votes = oldMenu.votes -1
                    oldMenu.save()
            menu = models.Menu.objects.get(day=day,restaurant = restaurant)
            employee.selectedMenu = menu
            menu.votes = menu.votes + 1
            menu.save()
            employee.save()
            return Response(status=status.HTTP_200_OK)

            
        except (models.employee.DoesNotExist,models.Restaurant.DoesNotExist,models.Menu.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(["GET"])
def mostVotedMenu(request,format=None):
    day = datetime.now().strftime('%A')
    menu = models.Menu.objects.order_by("-votes").filter(day=day).first()
    serializer = MenuSerializer(menu)
    return Response(serializer.data)
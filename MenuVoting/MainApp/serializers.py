from django.contrib.auth.models import User, Group
from rest_framework import serializers
from MainApp import models



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class RestaurantSerializer(serializers.ModelSerializer):
    name =serializers.CharField(max_length=50)
    menus = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    def create(self, validated_data):
        return models.Restaurant.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance
    
    class Meta:
        model = models.Restaurant
        fields=["name","menus"]


class MenuSerializer(serializers.ModelSerializer):
    contents = serializers.CharField(max_length=500)
    day = serializers.CharField(max_length = 20)
    restaurant = RestaurantSerializer()

    def create(self, validated_data):
        restaurant_data = validated_data.pop('restaurant')
        restaurant, _ = models.Restaurant.objects.get_or_create(name=restaurant_data["name"])

        return models.Menu.objects.create(restaurant=restaurant,**validated_data)
    
    def update(self, instance, validated_data):
        instance.contents = validated_data.get('contents',instance.contents)
        instance.day = validated_data.get('day',instance.day)
        instance.votes = validated_data.get('day',instance.votes)
        restaurant_data = validated_data.get('restaurant', instance.restaurant)
        restaurant, _ = models.Restaurant.objects.get_or_create(name=restaurant_data["name"])
        instance.restaurant = restaurant
        instance.save()
        return instance
    
    class Meta:
        model = models.Menu
        fields=["contents","restaurant","day","votes"]

class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    surname = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField(default="example@email.com")
    password = serializers.CharField(max_length=30)

    def create(self, validated_data):
        
        return models.employee.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.surname = validated_data.get("surname",instance.surname)
        instance.username = validated_data("username",instance.username)
        instance.email = validated_data("email",instance.email)
        instance.password = validated_data("password",instance.password)
        instance.save()
        return instance
    
    class Meta:
        model = models.employee
        fields=["name","surname","username","email","password"]

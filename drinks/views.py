from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

import drinks
from drinks.models import Drinks, Recipes
from drinks.serializers import DrinksSerializer, CategoriesSerializer, RecipesSerializer


###################################################### drinks
@api_view(['GET', 'POST'])
def drinksListAdd(request):
    if request.method == "GET":
        dr =Drinks.objects.all()
        drSer = DrinksSerializer(dr, many=True)
        return JsonResponse(drSer.data, safe=False)

    elif request.method == 'POST':
        drink = JSONParser().parse(request)
        print(drink)
        drinkSer =DrinksSerializer(data=drink)
        if  drinkSer.is_valid():
            drinkSer.save()
            return JsonResponse(drinkSer.data, status=status.HTTP_201_CREATED)
        print(drinkSer.errors)
        return JsonResponse(drinkSer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def drinksCat(request):
    if request.method == "GET":
        dr = Drinks.objects.all()
        drSer = CategoriesSerializer(dr, many=True)

        return JsonResponse(drSer.data, safe=False)

@api_view(['GET'])
def drinksOne(request, name):
    if request.method == 'GET':
        dr =Drinks.objects.filter(nume=name)
        drSerializer = DrinksSerializer(dr, many=True)
        return JsonResponse(drSerializer.data, safe=False)

@api_view(['DELETE'])
def deleteDrink(request, pk):
    tr = Drinks.objects.get(id=pk)
    if request.method == 'DELETE':
        tr.delete()
    return JsonResponse({'message': 'Drinks was deleted succesfully!'},
                        status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def updateDrink(request,pk):
    dr = Drinks.objects.get(id=pk)
    drink= JSONParser().parse(request)
    drserializer = DrinksSerializer(dr, data=drink)
    if drserializer.is_valid():
        drserializer.save()
        return JsonResponse(drserializer.data)
    return JsonResponse(drserializer.errors, status=status.HTTP_400_BAD_REQUEST)

##################################################################### recipes

@api_view(['GET', 'POST'])
def recipesListAdd(request):
    if request.method == "GET":
        dr =Recipes.objects.all()
        drSer = RecipesSerializer(dr, many=True)
        return JsonResponse(drSer.data, safe=False)

    elif request.method == 'POST':
        drink = JSONParser().parse(request)
        print(drink)
        drinkSer =RecipesSerializer(data=drink)
        if  drinkSer.is_valid():
            drinkSer.save()
            return JsonResponse(drinkSer.data, status=status.HTTP_201_CREATED)
        print(drinkSer.errors)
        return JsonResponse(drinkSer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def updateCat(request):
#     if request.method == "GET":
#         dr = Drinks.objects.all()
#         drSer = CategoriesSerializer(dr, many=True)
#         return JsonResponse(drSer.data, safe=False)

@api_view(['GET'])
def recipesById(request, pk):
    if request.method == 'GET':
        dr =Recipes.objects.filter(idBautura=pk)
        drSerializer = RecipesSerializer(dr, many=True)
        return JsonResponse(drSerializer.data, safe=False)

@api_view(['DELETE'])
def deleteRecipe(request, pk):
    tr = Recipes.objects.get(id=pk)
    if request.method == 'DELETE':
        tr.delete()
    return JsonResponse({'message': 'Recipe was deleted succesfully!'},
                        status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def updateRecipe(request,pk):
    dr = Recipes.objects.get(id=pk)
    drink= JSONParser().parse(request)
    drserializer = RecipesSerializer(dr, data=drink)
    if drserializer.is_valid():
        drserializer.save()
        return JsonResponse(drserializer.data)
    return JsonResponse(drserializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def drinksByCat(request, cat):
    if request.method == 'GET':
        dr =Drinks.objects.filter(categorie=cat)
        drSerializer = DrinksSerializer(dr, many=True)
        return JsonResponse(drSerializer.data, safe=False)

#fa functie care ia lista de nume a bauturilor dupa categorie
#fa in flutter un if in futureuilder
#adauga bauturile in lista iara daca apelul nu a mai fost facut atunci mai fa l
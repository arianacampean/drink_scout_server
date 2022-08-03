from rest_framework import serializers

from drinks.models import Drinks, Recipes


class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Drinks
        fields=('id','nume','modPreparare','categorie')

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Drinks
        fields=('categorie',)

class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipes
        fields=('id','idBautura','ingredient','cantitate','unitateDeMasura')

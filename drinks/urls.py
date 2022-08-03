from django.urls import path

from drinks import views

urlpatterns = [
    path('api/drinks/<str:name>', views.drinksOne),
    path('api/drinks', views.drinksListAdd),
    path('api/drinksCat/<str:cat>', views.drinksByCat),
    path('api/cat', views.drinksCat),
    path('api/deleteDr/<int:pk>', views.deleteDrink),
    path('api/updateDr/<int:pk>', views.updateDrink),
    path('api/recipes/<int:pk>', views.recipesById),
    path('api/recipes', views.recipesListAdd),
    path('api/deleteRe/<int:pk>', views.deleteRecipe),
    path('api/updateRe/<int:pk>', views.updateRecipe),

    ]
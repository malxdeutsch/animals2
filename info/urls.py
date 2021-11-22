from django.urls import path
from . import views

urlpatterns = [
    path('animals/<int:animal_id>', views.single_animal, name = 'animal'),
    path('families/<int:family_id>', views.single_family, name = 'family'),
    path('animals/', views.animal_all, name = 'all_animals'),
]
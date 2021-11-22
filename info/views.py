from django.shortcuts import render
from .models import Animal, Family

# Create your views here.
def single_family(request, family_id):
    family = Family.objects.get(id=family_id)
    return render(request, 'family.html', {'family':family})

def single_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'animal.html', {'animal':animal})

def animal_all(request):
    animals= Animal.objects.all()
    return render(request, 'animals.html', {'all_animals': animals})
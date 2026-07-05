from django.shortcuts import render, redirect
from .models import Food

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST['name']
        calories = request.POST['calories']

        Food.objects.create(
            name=name,
            calories=calories
        )

        return redirect('/')

    foods = Food.objects.all()

    total = sum(food.calories for food in foods)

    return render(request, 'index.html', {
        'foods': foods,
        'total': total
    })


def delete_food(request, id):
    food = Food.objects.get(id=id)
    food.delete()

    return redirect('/')


def reset(request):
    Food.objects.all().delete()
    return redirect('/')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Food
from .forms import FoodForm 

# Create your views here.
# Public
def show_main(request):
    foods = Food.objects.all().order_by('-created_at')
    context = {
        'app_name': 'Solomon Food Reviews',
        'foods': foods
    }
    return render(request, 'main.html', context)

def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    context = {'food': food}
    food.increment_views()
    return render(request, 'food_detail.html', context)

# Private
@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_food(request):
    form =  FoodForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('main:show_main')
    return render(request, 'add_food.html', context)
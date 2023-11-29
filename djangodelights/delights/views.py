from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, TemplateView
from django.db.models import Sum
from .models import MenuItem, RecipeRequirements, Ingredient, Purchase
from .forms import MenuItemForm, IngredientForm, RecipeRequirementsForm, PurchaseForm, InventoryUpdateForm


def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = MenuItemForm()

    return render(request, 'delights/add_menu_item.html', {'form': form})

def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    
    return render(request, 'delights/add_ingredient.html', {'form': form})

def add_recipe_requirements(request):
    if request.method == 'POST':
        form = RecipeRequirementsForm(request.POST)
        if form.is_valid():
            recipe_requirements = form.save()
            return redirect('menu')
    else:
        form = RecipeRequirementsForm()

    return render(request, 'delights/add_recipe_requirements.html', {'form': form})

def record_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase_list')
    else:
        form = PurchaseForm()

    return render(request, 'delights/record_purchase.html', {'form': form})

def update_inventory(request):
    if request.method == 'POST':
        form = InventoryUpdateForm(request.POST)
        if form.is_valid():
            ingredient = form.cleaned_data['ingredient']
            quantity = form.cleaned_data['quantity']

            ingredient.available_quantity += quantity
            ingredient.save()

            return redirect('ingredients_list')
    else:
        form = InventoryUpdateForm()

    return render(request, 'delights/update_inventory.html', {'form': form})

class HomeView(TemplateView):
    template_name = 'delights/home.html'


class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredient_list.html'
    context_object_name = 'ingredients'


class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'ingredient_confirm_delete.html'
    success_url = reverse_lazy('ingredient-list')


class MenuListView(ListView):
    model = MenuItem
    template_name = 'delights/menu_list.html'
    context_object_name = 'menu'


class PurchaseListView(ListView):
    model = Purchase
    template_name = 'delights/purchase_list.html'
    context_object_name = 'purchase_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class ProfitRevenueView(TemplateView):
    template_name = 'delights/profit_revenue.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        total_revenue = Purchase.objects.aggregate(Sum('menu_item__price'))[
            'menu_item__price__sum'] or 0
        context['total_revenue'] = total_revenue

        total_cost = RecipeRequirements.objects.aggregate(Sum('ingredient__price_per_unit'))[
            'ingredient__price_per_unit__sum'] or 0
        context['total_cost'] = total_cost

        profit = total_revenue - total_cost
        context['profit'] = profit

        return context

from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, TemplateView
from django.db.models import Sum
from .models import Ingredient, MenuItem, RecipeRequirements, Purchase


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

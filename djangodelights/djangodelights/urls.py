"""
URL configuration for djangodelights project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from delights.views import IngredientListView, IngredientDeleteView, MenuListView, PurchaseListView, ProfitRevenueView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingredients/', IngredientListView.as_view(), name='ingredient-list'),
    path('ingredient/<int:pk>/delete/', IngredientDeleteView.as_view(), name='ingredient-delete'),
    path('menu/', MenuListView.as_view(), name='menu-list'),
    path('purchases/', PurchaseListView.as_view(), name='purchase-list'),
    path('profit-revenue/', ProfitRevenueView.as_view(), name='profit-revenue'),
]

from django import forms
from django.forms import inlineformset_factory
from .models import MenuItem, RecipeRequirements, Ingredient, Purchase

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'price_per_unit', 'available_quantity', 'unit']

class RecipeRequirementsForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirements
        fields = ['ingredient', 'menu_item', 'quantity']

    def __init__(self, *args, **kwargs):
        super(RecipeRequirementsForm, self).__init__(*args, **kwargs)
        self.fields['ingredient'].queryset = Ingredient.objects.all()
        self.fields['menu_item'].queryset = MenuItem.objects.all()

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['menu_item', 'purchase_time']

class InventoryUpdateForm(forms.Form):
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all(), empty_label=None)
    quantity = forms.DecimalField(min_value=0, required=True, widget=forms.NumberInput(attrs={'step': 'any'}))
        

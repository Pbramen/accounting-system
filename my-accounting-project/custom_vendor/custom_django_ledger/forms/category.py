from django import forms
from custom_django_ledger.models.category import CategoryModel
from custom_django_ledger.models.entity import EntityModelProxy
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

class CategoryModelCreateForm(forms.ModelForm):
    name = forms.CharField(max_length = 32)
    description = forms.CharField(max_length = 128, required=False)

    class Meta:
        model = CategoryModel
        fields = [
            'name',
            'description',
        ]

    def __init__(self, *args, entity_slug=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.ENTITY = entity_slug


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if CategoryModel.objects.filter(name=name, entity__slug = self.ENTITY).exists():
            raise ValidationError("Category already exists.")
        return name


    def save(self, *args, commit=True, **kwargs):
        instance = super().save(commit=False)
        entity = get_object_or_404(EntityModelProxy.objects.filter(slug = self.ENTITY))
        
        instance.entity = entity
        if commit: 
            print('category being saved')
            instance.save()
        else:
            return instance
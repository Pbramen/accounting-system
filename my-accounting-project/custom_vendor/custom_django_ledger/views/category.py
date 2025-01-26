from django.views import generic
from custom_django_ledger.forms.category import CategoryModelCreateForm
from custom_django_ledger.models.category import CategoryModel
from .mixin import RecieveSuccessMsgMixin, CustomSecurityMixin
from django.urls import reverse_lazy


class CategoryMixin:
    model = CategoryModel
    context_object_name = 'category'


class CreateCategory(CustomSecurityMixin, CategoryMixin, generic.CreateView):
    form_class = CategoryModelCreateForm
    template_name_suffix = '_create' 

    def get_success_url(self):
        return reverse_lazy(
            'custom_django_ledger:category_view',
            kwargs={
                self.ENTITY_SLUG_URL_KWARG: self.kwargs.get(self.ENTITY_SLUG_URL_KWARG, ''), 
                'msg': self.kwargs.get('msg', None)
                }
            ) 

    def get_form_kwargs(self):
        kwargs =  super().get_form_kwargs()
        entity = self.kwargs.get(self.ENTITY_SLUG_URL_KWARG, None)
        kwargs[self.ENTITY_SLUG_URL_KWARG] = entity
        return kwargs


class ViewCategories(CustomSecurityMixin, RecieveSuccessMsgMixin, CategoryMixin, generic.ListView):
    template_name_suffix = '_view'
    
    def get_queryset(self):
        entity = self.kwargs.get(self.ENTITY_SLUG_URL_KWARG, None)
        return self.model.objects.for_entity(entity)


class UpdateSingleCategory(CustomSecurityMixin, RecieveSuccessMsgMixin, CategoryMixin, generic.UpdateView):
    template_name_suffix = '_update'
    fields = [
        'name',
        'description'
    ]

    def get_success_url(self):
        kwargs = self.kwargs
        kwargs['msg'] = 'Category Successfully Updated'
        return reverse_lazy('custom_django_ledger:category_update', kwargs = kwargs)

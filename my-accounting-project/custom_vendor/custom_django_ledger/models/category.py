from django.db import models
from django.utils.translation import gettext_lazy as _
from typing import Union
from uuid import UUID
from .entity import EntityModelProxy
from django.urls import reverse

class CategoryModelQuerySet(models.QuerySet):
    ...

class CategoryModelManager(models.Manager):
    def get_queryset(self) -> CategoryModelQuerySet:
        return CategoryModelQuerySet(self.model, using=self._db)

    def for_entity(self, entity_slug: Union[str, UUID, EntityModelProxy]):
        qs = self.get_queryset()

        if isinstance(entity_slug, EntityModelProxy):
            return qs.filter(entity=entity_slug)
        elif isinstance(entity_slug, UUID):
            return qs.filter(entity_id=entity_slug)
        return qs.filter(entity__slug__exact=entity_slug)
            
class CategoryModelAbstract(models.Model):
    '''
        An abstract class reprenting the set of catagories belogning to a specifc entity
            * note same named catagories may have different meaning among different entities
            * catagories are made for aggregating transactions (See models/transactions.py)

        Attributes:
        -----------
        
        - name: label of the category. Used in queries to select/group transactoins
        - description: a short optional value describing the category
        - entity: entity the category belongs to
    '''

    class Meta:
        abstract = True
        ordering = ['-name']
        constraints = [
            models.UniqueConstraint( 
                name='entity_categories',
                fields=['name', 'entity'])
            ]
        
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128, null=True)
    entity = models.ForeignKey(EntityModelProxy, on_delete=models.CASCADE)
    objects = CategoryModelManager()

    def get_absolute_url(self):
        return reverse("custom_django_ledger:category_update", kwargs={"entity_slug" : self.entity.slug, "pk": self.pk})
    
    
class CategoryModel(CategoryModelAbstract):
    class Meta:
        abstract = False
        
from django.db import models
from django.utils.translation import gettext_lazy as _

class CategoryModelQuerySet(models.QuerySet):
    ...

class CategoryModelManager(models.Manager):
    def get_queryset(self) -> CategoryModelQuerySet:
        return CategoryModelQuerySet(self.model, using=self._db)
        

class CategoryModelAbstract(models.Model):
    '''

        An abstract class reprenting the set of catagories belogning to a specifc entity
            * note same named catagories may have different meaning among different entities
            * catagories are made for aggregating transactions (See models/transactions.py)

        Attributes:
        -----------
        
        - name: label of the category. Used in queries to select/group transactoins
        - description: a short optional value describing the category
        - entity: entity this category belongs to
            accessible to any user that has access to this entity
    '''

    class Meta:
        abstract = True
        ordering = ['-name']

    name = models.CharField(max_length=32, null=False)
    description = models.CharField(max_length=128, null=True)
    
    objects = CategoryModelManager()

class CategoryModel(CategoryModelAbstract):
    class Meta:
        abstract = False

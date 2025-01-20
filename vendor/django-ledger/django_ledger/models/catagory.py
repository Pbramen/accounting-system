from django.db import models
from django_ledger.models import EntityModel
from typing import Optional, Union
from django.contrib.auth import get_user_model
from uuid import UUID
UserModel = get_user_model()


class CatagoryModelQuerySet(models.QuerySet):
    ...

class CatagoryModelManager(models.Manager):
    def get_queryset(self) -> CatagoryModelQuerySet:
        return CatagoryModelQuerySet(self.model, using=self._db)
    
    
    def for_entity(self, 
                   entity_slug: Union[str, EntityModel, UUID],
                ):
        qs = self.get_queryset()
        if entity_slug: 
            if isinstance(entity_slug, UUID):
                return qs.filter(entity_id = entity_slug)
            return qs.filter(entity__slug__exact = entity_slug)
        

class CatagoryModelAbstract(models.Model):
    '''

        An abstract class reprenting the set of catagories belogning to a specifc entity
            * note same named catagories may have different meaning among different entities
            * catagories are made for aggregating transactions (See models/transactions.py)

        Attributes:
        -----------
        
        - name: label of the catagory. Used in queries to select/group transactoins
        - description: a short optional value describing the catagory
        - entity: entity this catagory belongs to
            accessible to any user that has access to this entity
    '''

    class Meta:
        abstract: True

    name = models.CharField(max_length=32, null=False)
    description = models.CharField(max_length=128, null=True)
    entity = models.ForeignKey(EntityModel, on_delete=models.CASCADE)

    objects = CatagoryModelManager()

class CatagoryModel(CatagoryModelAbstract):
    class Meta:
        ordering = ['-entity', '-name']
        abstract = False

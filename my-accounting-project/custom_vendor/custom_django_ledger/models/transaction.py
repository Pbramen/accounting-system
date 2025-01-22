from django.db import models
from django_ledger.models import transaction # from third party 
from category import CategoryModel
from typing import Union

class CustomTransactionModelManager(transaction.TransactionModelManager):
    def for_category(self, category: Union[str, CategoryModel]):
        qs = self.get_queryset()
        if isinstance(category, str):
            return qs.filter(category__name__exact = category)
        if isinstance(category, CategoryModel):
            return qs.filter(category = category)
        return qs.none()

class TransactionProxyModel(transaction.TransactionModel):
    class Meta:
        proxy = True
    objects = CustomTransactionModelManager()    
    
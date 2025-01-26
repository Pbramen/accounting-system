'''
    Custom Transaction Proxy to extend base functionality of Django-ledger's transaction model class.

    Adds a new field: category
        -> Grouping at transaction layer
'''
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
    
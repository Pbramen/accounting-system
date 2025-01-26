from django_ledger.models.entity import EntityModel

class EntityModelProxy(EntityModel):
    class Meta:
        swappable = None
        proxy = True

from typing import Any
from django_ledger.views.mixins import DjangoLedgerSecurityMixIn


class RecieveSuccessMsgMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('this success mixin in ')
        msg = self.kwargs.get('msg') or self.request.GET.get('msg') or None
        if msg:
            context['msg'] = msg
        print(msg)
        return context
    

# redirects if entity_slug is not valid
class CustomSecurityMixin(DjangoLedgerSecurityMixIn):
    # TODO: replace get login url
    def get_login_url(self):
        return ''
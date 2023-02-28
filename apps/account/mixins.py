from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin

class SuperUserOnlyMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_admin:
                return super().dispatch(request, *args, **kwargs)

        return HttpResponseForbidden()
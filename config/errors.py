from django.views import View
from django.shortcuts import render


class PageNotFoundView(View):
    status = 404
    template_name = '404.html'

    def get(self, request, exception=None):
        return render(request=request, template_name=self.template_name, status=self.status)

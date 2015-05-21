# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf.urls import url

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

# class OnePageAppView(TemplateView):
#     template_name = 'index.html'

class AboutView(TemplateView):
    template_name = "index.html"

class DjangularModuleTemplateView(TemplateView):
    content_type = 'text/javascript'
    template_name = 'app.js'
    disable_csrf_headers = False

    def get_context_data(self, **kwargs):
        context = super(DjangularModuleTemplateView, self).get_context_data(**kwargs)
        context['disable_csrf_headers'] = self.disable_csrf_headers
        return context

# then in the views, from https://speakerdeck.com/pycon2014/straightening-out-angularjs-with-python-by-jeff-schenck
# from django.shortcuts import render
# def render_partial(request, template_name=None):
#     template_name = 'partials/{}'.format(template_name)
#     context = {
#         'you-are-a-unique-snowflake': True,
#     }
#     return render(request, template_name, context)
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import AboutView, DjangularModuleTemplateView

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]

urlpatterns = [
    url(r'^$', AboutView.as_view()),
    # OOOOR you can do this
    # url(r'^$', TemplateView.as_view(template_name="index.html")),
    # url(r'^djangular/', include('djangular.urls')),
    url(r'^$', TemplateView.as_view(template_name="app.js"))
    # url(r'^app.js$', DjangularModuleTemplateView.as_view(), name='app.js')
]


# urlpatterns = [
    # url(r'^djangular/', include('djangular.urls')),
    # url(r'^$', views.OnePageAppView.as_view(), name='home')
# ]
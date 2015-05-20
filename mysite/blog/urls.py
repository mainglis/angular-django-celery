from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import AboutView

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]

urlpatterns = [
    url(r'^$', AboutView.as_view()),
    # OOOOR you can do this
    # url(r'^$', TemplateView.as_view(template_name="index.html")),
]


# urlpatterns = [
    # url(r'^djangular/', include('djangular.urls')),
    # url(r'^$', views.OnePageAppView.as_view(), name='home')
# ]
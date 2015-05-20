from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

# urlpatterns = [
    # url(r'^djangular/', include('djangular.urls')),
    # url(r'^$', views.OnePageAppView.as_view(), name='home')
# ]
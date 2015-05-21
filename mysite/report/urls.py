from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import views
from views import index, SamplePartial

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.partial, name='partial'),
     # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^$', TemplateView.as_view(template_name="index1.html")),
    # url(r'^rendered-partials/(?P<template_name>.*)$', 'render_partial'),
    # url(r'^partials/', TemplateView.as_view(template_name="partial2.html")),
    # url(r'^partials/(?P<template_name>[-_\w]+/$)', SamplePartial.as_view(), name='partials'),
    # url(r'^partials/(?P<folder>[-_\w]+)/(?P<template_name>[-_\w]+/$)', SamplePartial.as_view(), name='partials_folder'),
    # url(r'^partials/', TemplateView.as_view(template_name="partial1.html")),
    # # url(r'^djangular/', include('djangular.urls')),
    # url(r'^$', TemplateView.as_view(template_name="app.js"))
    # # url(r'^app.js$', DjangularModuleTemplateView.as_view(), name='app.js')
]

urlpatterns += staticfiles_urlpatterns()

print urlpatterns

# var_url = url(r'^partials/(?P<template_name>[-_\w]+/$)', SamplePartial.as_view(), name='partials')
# print var_url
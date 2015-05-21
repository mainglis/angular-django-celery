from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index1.html")),
    # url(r'^partials/', TemplateView.as_view(template_name="partial1.html")),
    # # url(r'^djangular/', include('djangular.urls')),
    # url(r'^$', TemplateView.as_view(template_name="app.js"))
    # # url(r'^app.js$', DjangularModuleTemplateView.as_view(), name='app.js')
]

urlpatterns += staticfiles_urlpatterns()
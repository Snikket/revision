from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'revision.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dev/', 'views.dev', name='dev'),
    url(r'^admin/', include(admin.site.urls)),
)

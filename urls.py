from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
      url(r'^$', 'News.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
      url(r'^$', 'News.views.newspage', name='newspage'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

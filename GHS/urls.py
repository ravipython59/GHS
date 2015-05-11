from django.conf.urls import patterns, include, url
#import pdb
from django.contrib import admin
admin.autodiscover()
#pdb.set_trace()
urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'Services.views.home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'Services.views.login'),
    url(r'^test_login/', 'Services.views.test_login'),
    url(r'^register/', 'Services.views.register'),
    url(r'^register_user/', 'Services.views.register_user'),
)

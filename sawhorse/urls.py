from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()


app_urls = []
for app_name in settings.INSTALLED_APPS:
    if app_name.startswith('django.contrib'):
        # don't include contrib apps
        # admin apps are included explicitly below
        continue
    app_label = app_name.rsplit('.', 1)[-1]
    try:
        app_urls.append(url('^%s/' % app_label, include('%s.urls' % app_name)))
    except ImportError:
        pass

app_urls.extend([
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
])

urlpatterns = patterns('', *app_urls)

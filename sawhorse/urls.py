from django.urls import include, path
from django.conf import settings

from django.contrib import admin


urlpatterns = []
for app_name in settings.INSTALLED_APPS:
    if app_name.startswith('django.contrib'):
        # don't include contrib apps
        # admin apps are included explicitly below
        continue
    app_label = app_name.rsplit('.', 1)[-1]
    try:
        urlpatterns.append(path('^%s/' % app_label, include('%s.urls' % app_name)))
    except ImportError:
        pass

urlpatterns.extend([
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
])

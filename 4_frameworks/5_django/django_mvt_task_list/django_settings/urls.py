from django.shortcuts import redirect
from django.urls import path, include, re_path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('django_app.urls')),
]

urlpatterns += [re_path(r'^.*$', lambda request: redirect('', permanent=False), name='redirect')]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
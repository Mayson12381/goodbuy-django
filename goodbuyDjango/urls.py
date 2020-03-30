from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('goodbuyApi.urls')),
    path('', include('auth0authorization.urls'))
 ]

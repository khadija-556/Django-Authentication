from django.urls import path,include

urlpatterns = [
    path('api/v1/', include('apps.authentication.urls')),
    #path('api/v1/', include('apps.authentication.search.urls')),

] 
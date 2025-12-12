from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('todos/', include('todos.urls')),
    path("depl/", include("depl.urls")),
    path("reports/", include("reports.urls")),



    path('api/', include('rest_framework.urls')),  # Browsable login
]

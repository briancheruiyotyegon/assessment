from django.contrib import admin
from django.urls import path, include,re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view=get_schema_view(
    openapi.Info(
        title="Health API",
        default_version='v1',
        description="Health API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="meshackyegon10@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', include('health.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='schema-json'),

]

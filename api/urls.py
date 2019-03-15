from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

app_name = 'api'

schema_view = get_swagger_view(title='Pastebin API')

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]

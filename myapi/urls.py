from django.urls import include, path
from rest_framework import routers
from . import views
from django.http import JsonResponse

router = routers.DefaultRouter()
router.register(r'locations', views.LocationViewSet)
router.register(r'images', views.ImageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('places/', views.places, name='places'),
    path('places/<str:latitude>/<str:longitude>', views.nearest_places, name="nearest_places"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

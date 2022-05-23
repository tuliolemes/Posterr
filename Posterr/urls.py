from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from posts import views as post_view
from profiles import views as profile_view

router = routers.DefaultRouter()
router.register(r'profiles', profile_view.ProfileViewSet)
router.register(r'posts', post_view.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
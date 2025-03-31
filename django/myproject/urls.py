
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from polls.nocodb_utils_v2 import get_nocodb_data
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('nocodb-data/', get_nocodb_data, name='nocodb_data'),

]

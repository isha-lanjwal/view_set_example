from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

# creating router object
router = DefaultRouter()

# Register StudentViewSet with Router(viewset)
# router.register('studentApi',views.StudentViewSet,basename='student')

# Register StudentViewSet with Router(model viewset)
router.register('studentApi',views.StudentModelViewSet,basename='student')

# readonly
# router.register('studentApi_rd',views.StudentReadOnlyModelViewSet,basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include(router.urls))
]

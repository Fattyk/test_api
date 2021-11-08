from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('simple', views.TestViewset)
urlpatterns = [
    path('', views.TestListCreate.as_view()), #api
    path('<int:id>/', views.TestDetail.as_view()), #api/{id}
    path('easy/', include(router.urls)) #api/easy/
]
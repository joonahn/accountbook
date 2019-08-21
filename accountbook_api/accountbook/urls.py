from django.urls import path, include
from accountbook import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'accountbook', views.AccountBookDataViewSet, 'accountbook')
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AccountBookDataViewSet, AccountViewSet, CategoryViewSet, UserViewSet

router = DefaultRouter()
router.register(r'accountbook', AccountBookDataViewSet, 'accountbook')
router.register(r'account', AccountViewSet, 'account')
router.register(r'category', CategoryViewSet, 'category')
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

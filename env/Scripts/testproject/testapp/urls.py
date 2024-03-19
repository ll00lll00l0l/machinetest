from django.urls import path,include
from testapp import views 
from rest_framework import routers

router =  routers.DefaultRouter()
router.register(r'diver', views.DriverViewSet, 'post')
router.register(r'Ride', views.RideViewSet, 'get')
urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.user_login, name='login'),
    path('test_token/', views.test_token, name='test'),
    path('User/', include(router.urls)),
    # path('logout/', user_logout, name='logout'),
]
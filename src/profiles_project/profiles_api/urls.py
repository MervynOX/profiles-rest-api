from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet) # because it is a model viewset, therefore basename is not needed
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)
router.register('events', views.EventProfileViewSet)

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    #router object will create the url for us, but checking if any of the url matches the condition first
    url(r'', include(router.urls))
]

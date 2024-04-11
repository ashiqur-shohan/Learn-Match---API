from rest_framework.routers import DefaultRouter
from django.urls import include,path
from .views import TeacherViewset,UserRegistrationApiview,UserLoginApiView,UserLogoutView,activate,ChangePasswordView,UserViewSet,logout_view,TeacherImageView


router = DefaultRouter()

router.register('list',TeacherViewset)


urlpatterns = [
    path('',include(router.urls)),
    path('register/',UserRegistrationApiview.as_view(),name='register'),
    path('login/',UserLoginApiView.as_view(),name='login'),
    path('data/<int:pk>',UserViewSet.as_view(),name='data'),
    path('image/<int:pk>',TeacherImageView.as_view(),name='user_image'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    # path('logout/',logout_view,name='logout'),
    path('active/<uid64>/<token>',activate,name='activate'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]

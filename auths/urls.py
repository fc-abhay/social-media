from django.urls import path
from .views import registerView, loginView, getUserDetails,getOtherUserInfo,updateProfileView,deleteUserView

urlpatterns = [
    path('register/',  registerView),
    path('login/',  loginView),
    path("get-user-info/",getUserDetails),
    path("profile/<uuid:pk>",getOtherUserInfo),
    path("update-profile/",updateProfileView),
    path("delete-profile/",deleteUserView)
]

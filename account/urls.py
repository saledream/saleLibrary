from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views 

urlpatterns = [

    path("login/",views.user_login,name="login"),
    path("logout/",views.user_logout,name="logout"),
    path("sign-up/",views.user_signup,name="signup"),
    path("reset_password/",auth_views.PasswordResetView.as_view(success_url="/accounts/password_reset_done/"), name="reset_password"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("reset_password/confirm/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(success_url="/accounts/reset_password_complete/"),name="password_reset_confirm"),
    path("reset_password_complete/",auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path("password-change/",views.password_change,name="pwd_change"),
    path("show-MyProfile",views.showMyProfile,name="show_profile"),
    path("edit-MyProfile/",views.editMyProfile,name="editMyProfile"),
]
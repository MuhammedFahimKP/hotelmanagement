from django.urls import path

from . import views


urlpatterns = [
    
    path('signup/',views.UserSignUpAPIView.as_view(),name="signup"),
    path('signin/',views.UserSignInAPIView.as_view(),name="signin"),
    path('google-auth/',views.UserGoogleAuthAPIView.as_view(),name="google-auth"),
    
]

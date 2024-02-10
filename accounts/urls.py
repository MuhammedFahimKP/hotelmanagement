from django.urls import path

from . import views


urlpatterns = [
    
    path('signup/',views.UserSignUpAPIView.as_view(),name="signup"),
    path('signin/',views.UserSignInAPIView.as_view(),name="signin"),
    
]

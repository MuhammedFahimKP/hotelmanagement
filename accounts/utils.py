from django.conf import settings
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth.hashers import make_password


from rest_framework.exceptions import AuthenticationFailed

from google.oauth2 import id_token
from google.auth.transport import requests



USER = get_user_model()

class Google:
     
    @staticmethod 
    def validate(access_token):
        
        try:     
                
            id_info = id_token.verify_oauth2_token(access_token,requests.Request(),settings.GOOGLE_CLIENT_ID)
            if 'accounts.google.com' in id_info['iss']:
                return id_info
                

        except Exception as e:
                return "Token is Invalid or has expired"    
    

def login_user(email):
    
    social_user = authenticate(email=email,password=settings.SOCIAL_AUTH_PASSWORD)
    
    return {
            
        "email":social_user.email,
        "first_name":social_user.first_name,
        "last_name" : social_user.last_name,
        "access":f"{social_user.tokens['access']}",
        "refresh":f"{social_user.tokens['refresh']}"                            
    }


def register_social_user(email,first_name,last_name,auth_provider):
                
    user = USER.objects.filter(email=email)
    
    if user.exists():
        
        if  user.first().auth_provider == auth_provider:                               
            
            return login_user(email)           
        
        else:
            return f'please login with your {user[0].auth_provider} account '
            
    else:
        
        user_data = {
            
                'email':email,
                'first_name':first_name,
                'last_name':last_name,
                'password': make_password(settings.SOCIAL_AUTH_PASSWORD)       
        }

        register_user = USER.objects.create(**user_data)
        register_user.auth_provider = 'google'
        register_user.is_active = True
        register_user.save() 
        return login_user(email=email)
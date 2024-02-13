from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

from rest_framework import serializers


USER = get_user_model()


class UserSignUpSerializer(serializers.ModelSerializer):
    
    
    email            = serializers.EmailField(max_length=100)
    first_name       = serializers.CharField(max_length=50)
    last_name        = serializers.CharField(max_length=50)
    password         = serializers.CharField(min_length=8,max_length=16,write_only=True)      
    confirm_password = serializers.CharField(min_length=8,max_length=16,write_only=True)
    
    
    def validate(self, data:dict) -> dict:
        
        user = USER.objects.filter(email=data['email']) 
        if user.exists():
            
            raise serializers.ValidationError({
                'email':'email  have already registered' 
            })
        
                 
        if data['password'] != data['confirm_password'] :
            
            raise serializers.ValidationError({'password':'passwords are not matching'})
                    
        return data    
    
    def create(self,validated_data:dict) -> object:
        validated_data['password'] = make_password(validated_data['password'])
        validated_data.pop('confirm_password')
        return super().create(validated_data)
        
               
    
    class Meta:
        
        model  = USER
        fields = [
            
            'email',
            'first_name',
            'last_name',
            'password',
            'confirm_password',

        ]
        
        
        

class UserSignInSerializer(serializers.Serializer):
    
    email          = serializers.EmailField(max_length=100)
    first_name     = serializers.CharField(read_only=True)
    last_name      = serializers.CharField(read_only=True)
    password       = serializers.CharField(write_only=True)
    access         = serializers.CharField(read_only=True)
    refresh        = serializers.CharField(read_only=True)
   
   
    
    
    
    
    
    
    def validate(self,data):
       
        email    = data['email']
        password = data['password']
        

        user = USER.objects.filter(email__iexact=email)

        if not user.exists():
            raise serializers.ValidationError({
                'email':'User not found please register'
            })
            
        user = user.first()
        if user.check_password(password) == False:
            raise serializers.ValidationError({
                'passowrd':'incorrect password'
            })
            
        if user.is_active == False:
            raise serializers.ValidationError({
                'user':'is not verfied'
            })

        return {
            'email':user.email,
            'first_name':f"{user.first_name}",
            'last_name':f'{user.last_name}',
            'access':str(user.tokens.get('access')),
            'refresh':str(user.tokens.get('refresh'))
        }
        
        
        
    
    
    
    class Meta:
        fields = [
            'firs_name',
            'last_name',
            'email',
            'password',
            'access',
            'refresh',
            
        ],
        
        
        
        
    
    
    
from rest_framework import serializers
from .models import MyUser




class UserSignupSerializer(serializers.ModelSerializer):
    
    
    email            = serializers.CharField(max_length=100)
    first_name       = serializers.CharField(max_length=50)
    last_name        = serializers.CharField(max_length=50)
    password         = serializers.CharField(min_length=8,max_length=16,write_only=True)      
    confirm_password = serializers.CharField(min_length=8,max_length=16,write_only=True)
    
    
    def validate(self, data:dict) -> dict:
        
        user = MyUser.objects.filter(email=data['email']) 
        if user.exists():
            
            raise serializers.ValidationError({
                'email':'email already exists'
            })
        
                 
        if data['password'] != data['confirm_password'] :
            
            raise serializers.ValidationError({'password':'passwords are not matching'})
                    
        return data    
    
    def create(self,validated_data:dict) -> MyUser:        
        validated_data.pop('confirm_password')
        return super().create(validated_data)
        
               
    
    class Meta:
        
        model  = MyUser
        fields = [
            
            'email',
            'first_name',
            'last_name',
            'password',
            'confirm_password',

        ]
        
        
        


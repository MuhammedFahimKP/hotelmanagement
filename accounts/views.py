from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics,renderers,status


from .serializers import (
    
    UserSignUpSerializer,
    UserSignInSerializer,
    UserGoogleAuthSerializer

)
from .models import MyUser



# Create your views here.



class UserSignUpAPIView(generics.GenericAPIView):
    
    queryset         = MyUser.objects.all()
    serializer_class = UserSignUpSerializer
    # renderer_classes = [renderers.JSONOpenAPIRenderer]          
       

    #post method only allow

    def post(self,request)-> Response:

        #taking the post data   
        user_data = self.request.data

        #sending the data to the serializer
        serializer = self.serializer_class(data=user_data)

        """
        checking serializer is valid if serialzer is not valid it will send serailizor error with http 400   

        """    
        if serializer.is_valid(raise_exception=True):

            #creating new user  object using serializer create method
            
            serializer.save()

            #taking the serializer data for response sending activation link

            
            
            #calling thread class to send email

            # EmailThread(req=self.request,user=user).start()
            
            #returning the response with http 201
          
            return Response({
                serializer.data
            },status=status.HTTP_201_CREATED) 
         
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 



    
    
class UserSignInAPIView(generics.GenericAPIView):

    
    serializer_class = UserSignInSerializer

    #allow only post method
    def post(self,request):
        #passing the data to the serializer
        serialzer = self.serializer_class(data=self.request.data)
         
        #if serializer valid then it will send a data with http 200 
        if serialzer.is_valid(raise_exception=True):
            return Response(serialzer.data,status=status.HTTP_200_OK)
        
        #otherwise it will send data serializer error with http 400 
        return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
    
        
        
class UserGoogleAuthAPIView(generics.GenericAPIView):

    
    serializer_class = UserGoogleAuthSerializer

    #allow only post method
    def post(self,request):
        
        #passing the data to the serializer
        serialzer = self.serializer_class(data=self.request.data)
         
        #if serializer valid then it will send a data with http 200 
        if serialzer.is_valid(raise_exception=True):
            
            return Response(serialzer.data,status=status.HTTP_200_OK)

        
        #otherwise it will send data serializer error with http 400
        
        print("error",serialzer.errors)
        
        return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
            
        
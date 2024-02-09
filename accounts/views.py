from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics,renderers,status


from .serializers import UserSignupSerializer
from .models import MyUser



# Create your views here.



class UserSignupView(generics.GenericAPIView):
    
    queryset         = MyUser.objects.all()
    serializer_class = UserSignupSerializer
    renderer_classes = [renderers.JSONOpenAPIRenderer]          
       

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

            user = serializer.data
            
            #calling thread class to send email

            # EmailThread(req=self.request,user=user).start()
            
            #returning the response with http 201

          
            return Response({
                'data':user,
                'message':f"hi {user['first_name']} thanks for siging up",
            },status=status.HTTP_201_CREATED) 
         
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        
        
from django.shortcuts import render,redirect
from .serializers import TeacherSerializer,RegistrationSerializer,UserLoginSerializer,ChangePasswordSerializer,UserSerializer,TeacherImageSerializer
from .models import TeacherModel,TeacherImageModel
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_204_NO_CONTENT,HTTP_200_OK
from rest_framework.decorators import api_view

from rest_framework import viewsets,generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout

from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from rest_framework.response import Response
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class TeacherViewset(viewsets.ModelViewSet):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get("user_id")
        if user_id:
            queryset = queryset.filter(user = user_id)
        return queryset
    
    def put(self,request):
        user_id = self.request.query_params.get("user_id")
        if user_id:
            data = TeacherModel.objects.get(user=user_id)
            serializers = TeacherSerializer(data, data=request.data)
            print(serializers)
            print("inside user_id before serializers")
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)

@api_view(["POST",])
def image_post(request,pk):
        
        serializers = TeacherImageSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response (serializers.data)
        return Response({"error":"Input wrong"},HTTP_400_BAD_REQUEST)


class TeacherImageView(APIView):
    serializer_class = TeacherImageSerializer
    def get_queryset(self,request,pk):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=pk)
        return queryset
    def get(self,request,pk):
        data_list = TeacherImageModel.objects.filter(user=pk)
        data_length = len(data_list) - 1
        data = data_list[data_length]
        serializer = TeacherImageSerializer(data , context={'request': request})
        return Response(serializer.data)
    
    def put(self,request,pk):
        data = TeacherImageModel.objects.get(user=pk)
        serializers = TeacherImageSerializer(data, data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response (serializers.data)
        return Response({"error":"Input wrong"},HTTP_400_BAD_REQUEST)

class UserViewSet(APIView):
    # queryset = TeacherModel.objects.all()
    serializer_class = UserSerializer    
    def get_queryset(self,request,pk):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk = pk)
        return queryset 
    def get(self,request,pk):
        data = User.objects.get(pk=pk)
        serializer = UserSerializer(data)
        return Response(serializer.data)
    def put(self,request,pk):
        data = User.objects.get(pk=pk)
        serializers = UserSerializer(data, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
    
class UserRegistrationApiview(APIView):
    serializer_class = RegistrationSerializer

    #apiview te bole dite hoy ki type request kora hbe get nki post nki onno kichu
    #jokhn e user post krbe tkhn e data ta pass hbe nicer maddhome
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            
            # user er unique id create hbe
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print('uid',uid)
            # confirm_link = f"http://127.0.0.1:8000/user/active/{uid}/{token}"
            confirm_link = f"https://learn-match-api.onrender.com//user/active/{uid}/{token}"
            email_subject = "Confirm your email"
            email_body = render_to_string('confirm_email.html',{'confirm_link':confirm_link})
            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()

            #ei return gula backend theke amra pathacchi. front end a response a eigula pabe. pore js .then diye ei response gula catch korbe
            return Response('Check Your mail for confirmation')
        return Response(serializer.errors)
    
#account activate korar jonno
def activate(request,uid64,token):
    try:
        #uid ta ke decode kortese
        uid = urlsafe_base64_decode(uid64).decode()
        #decode kora uid ta kon user er sheita ber kore niye ashtese
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        # return redirect ('login')
        return redirect ('http://127.0.0.1:5500/login.html')

    else:
        return redirect('register')

#login er jonno shudhu post request
# login kora mane ultimately ekta token create kora user er jonno jodi user ta valid user hoy
class UserLoginApiView(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username,password=password)

            if user:
                #token jodi thake tahole get kore niye ashbe na hole create korbe
                #jehetu get or create jei kono ekta hbe tai dui var disi
                # token use krte hole setting a jeye installed app a bole diye ashte hbe
                #migrate command dite hbe
                token,_ = Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({'token':token.key,'user_id' : user.id})
            else:
                return Response({'error':'Invalid Credential'})
        return Response(serializer.errors)

class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        logout(request)
        return Response({'message': 'Logout successful.',}, status=HTTP_204_NO_CONTENT)


class ChangePasswordView(APIView):
    def put(self, request):
        user_id = request.data.get("user_id")
        users = User.objects.get(pk=user_id)
        serializer = ChangePasswordSerializer(data=request.data, context={'user': users})
        if serializer.is_valid():
            
            # user = request.user
            users.set_password(serializer.validated_data['new_password'])
            users.save()
            return Response({'message': 'Password changed successfully.'})
        print("before return error")
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
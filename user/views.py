from django.shortcuts import render,redirect
from .serializers import TeacherSerializer,RegistrationSerializer,UserLoginSerializer
from .models import TeacherModel
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.views import APIView

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout

from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from rest_framework.response import Response
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

class TeacherViewset(viewsets.ModelViewSet):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer


class UserRegistrationApiview(APIView):
    serializer_class = RegistrationSerializer

    #apiview te bole dite hoy ki type request kora hbe get nki post nki onno kichu
    #jokhn e user post krbe tkhn e data ta pass hbe nicer maddhome
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print('token',token)
            
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
        return redirect ('login')
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
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from  rest_framework.permissions import DjangoModelPermissions,IsAuthenticated
from.models import Fruit
from rest_framework.response import  Response
from.serializers import fruitserializers,registrationserializers,LoginSerializer,profileserializers,chanegserializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import  authenticate
from.models import Fruit



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class register(APIView):
    def post(self,request):
        info=request.data
        serializers=registrationserializers(data=info)
        if serializers.is_valid():
            USER=serializers.save()
            token=get_tokens_for_user(USER)
            return Response({"succeess":token})
        return Response({"Errors":[serializers.errors]})

class LoginView(APIView):
    def post(self, request,):
        serializer =LoginSerializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            name=serializer.validated_data['username']
            passs = serializer.validated_data['password']
            user =authenticate(request=self.request,username=name,password=passs)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({"Sucsses":token})
            else:
                return Response({"Errors": "There is no user"})

        else:
            return Response({"Errors": [serializer.errors]})

class profile(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        serializers=profileserializers(request.user)
        return Response(serializers.data)

class changepassword(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serializers=chanegserializers(data=self.request.data,context={"user":request.user})
        if serializers.is_valid():
            return Response({"MSG":"Jio done dona done"})
        return Response({"Errors":serializers.errors})


def names(name):
    geting = Fruit.objects.all()
    for i in geting:
        if name.lower()==i.Name.lower():
            return Fruit.objects.get(Name=i.Name)

class fruitnutrition(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [DjangoModelPermissions]
    def get(self,request,name=None):
            if name is not None:
                 if names(name):
                    serializer=fruitserializers(names(name))
                    return Response(serializer.data)
                 return Response({"Errors": "There no any fruit of such name "})
    def put(self,request,name=None):
        if names(name):
            serializer=fruitserializers(names(name),data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Done":"Put done"})
            return Response(serializer.data)
        return Response({"Errors": "There no any fruit of such name "})
    def patch(self,request,name=None):
        if names(name):
             serializer = fruitserializers(names(name), data=self.request.data,partial=True)
             if serializer.is_valid():
                 serializer.save()
                 return Response({"Done": "Patch done"})
             return Response(serializer.data)
        return Response({"Errors": "There no any fruit of such name "})

    def delete(self,request,name=None):
        if names(name):
            names(name).delete()
            return Response({"Done": "Delete done"})
        return Response({"Errors": "There no any fruit of such name "})


class allfruit(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [DjangoModelPermissions]
    def get(self, request):
        geting = Fruit.objects.all()
        serializer = fruitserializers(geting,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = fruitserializers(data=self.request.data)
        if serializer.is_valid():
            name=serializer.validated_data["Name"]
            if  Fruit.objects.filter(Name=name).exists():
                return Response({"Errors": "Fruit Details already exists"})
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)
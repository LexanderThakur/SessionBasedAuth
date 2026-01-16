import jwt
import json

from django.http import JsonResponse
from api.models import User
from django.contrib.auth.hashers import make_password,check_password

from datetime import datetime, timedelta
from django.conf import settings

def register(request):
    data= json.loads(request.body)


    user_email= data["user_email"]
    user_password= data["user_password"]

    user = User.objects.filter(user_email=user_email).first()
    if user:
        return JsonResponse({"message":"user already exist"})
    
    user = User(
        user_email=user_email,
        user_password=make_password(user_password)
    )
    user.save()

    payload={
        "user_id":user.id,
        "user_email":user.user_email,
        "exp":datetime.utcnow() + timedelta(minutes=50)
    }

    encoded_jwt= jwt.encode( payload,settings.JWT_SECRET,algorithm="HS256"   )

    return JsonResponse({"message":"successfully registered","jwt":encoded_jwt})

def login(request):
    data= json.loads(request.body)


    user_email= data["user_email"]
    user_password= data["user_password"]

    
    
    user=User.objects.filter(user_email=user_email).first()
    if not user:
        return JsonResponse({"message":"user does not exist"})
    
    if not check_password(user_password,user.user_password):
        return JsonResponse({"message":"wrong password"})
    


    payload={
        "user_id":user.id,
        "user_email":user.user_email,
        "exp":datetime.utcnow() + timedelta(minutes=50)
    }


    encoded_jwt= jwt.encode( payload,settings.JWT_SECRET,algorithm="HS256"   )

    return JsonResponse({"message":"successfully registered","jwt":encoded_jwt})


def me(request):
    

    user= request.user

    user_q= User.objects.filter(id=user).first()


    return JsonResponse({"message":f"user with email {user_q.user_email} is see you baby!!"})


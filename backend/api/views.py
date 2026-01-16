from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse,JsonResponse
import uuid
from .import Session,User

from django.contrib.auth.hashers import make_password, check_password
def home(request):
    return render(request,"index.html")



def login(request):
    data= json.loads(request.body)

    user_email= data.get("user_email",None)
    user_pass= data.get("user_password",None)
    user = User.objects.filter(user_email=user_email).first()

    if not user:
        return JsonResponse({"message":"user does not exist"})
    
    if not check_password(user_pass,user.user_password):
        return JsonResponse({"message":"wrong password"})

    session=Session.objects.filter(user_email=user_email)
    if session:
        session.delete()
        
    
    session_id= uuid.uuid4()
    session= Session(session_id=session_id,user_email=user)

    session= Session(session_id=session_id,user_email=user)
    session.save()

    return JsonResponse({"message":"logged in","session_id":session_id})

def register(request):
    data=json.loads(request.body)
    user_email= data.get("user_email",None)
    user_pass= data.get("user_password",None)
    if User.objects.filter(user_email=user_email):
        return JsonResponse({"message":"user alreay exists"})
    
    hashed_password= make_password(user_pass)

    user= User(user_email=user_email,user_password=hashed_password)
    user.save()

    session_id= uuid.uuid4()

    session= Session(session_id=session_id,user_email=user)
    session.save()
    return JsonResponse({"message":"successfully registered"})






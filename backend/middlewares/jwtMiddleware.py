
import jwt
from django.http import JsonResponse
from django.conf import settings

class JWTMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        self.public_paths = [
            "/",
            "/login/",
            "/register/",
            "/jwt/login/",
            "/jwt/register/",
            "/static/",
            "/.well-known/",
        ]

    def __call__(self, request):
        if request.path in self.public_paths:
            return self.get_response(request)
        
        request.user=None
        auth=request.headers.get("Authorization")
        if not auth:    
            return JsonResponse({"error": "Unauthorized"}, status=401)
        
        try:
            scheme,token=auth.split()

            payload=jwt.decode(token,settings.JWT_SECRET,algorithms='HS256')
            request.user=payload['user_id']


        except Exception as e:
              return JsonResponse({"error": str(e)}, status=401)

        return self.get_response(request)

        

    
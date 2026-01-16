

from api.models import Session



class AuthMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self, request):

        token=request.headers.get("Authorization")

        request.user=None

        if token:
            q=Session.objects.filter(session_id=token).first()
            if q:
                request.user=q.user_email
                return self.get_response(request)
            
        return self.get_response(request)
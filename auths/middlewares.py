import jwt
from django.conf import settings
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from .models import Auth

SECRET_KEY = settings.SECRET_KEY

EXEMPT_URLS = [
    '/v1/api/auth/login/',
    '/v1/api/auth/register/',
]

class JWTAuthenticationMiddleware(MiddlewareMixin):
    """
    Middleware to parse JWT from Authorization header.
    Attach payload and Auth model instance to request if valid.
    """

    def process_request(self, request):
        path = request.path

        # Skip exempt URLs
        if any(path.startswith(url) for url in EXEMPT_URLS) or path.startswith('/admin/'):
            return None

        # Skip OPTIONS requests (CORS preflight)
        if request.method == "OPTIONS":
            return None

        request.token_payload = None
        request.token_user = None

        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return JsonResponse({"message": "Authorization header missing"}, status=401)

        try:
            parts = auth_header.split()
            if len(parts) != 2 or parts[0].lower() != "bearer":
                raise ValueError("Invalid token header format")

            token = parts[1]
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.token_payload = payload

            # Attach Auth model instance, NOT serializer.data
            try:
                user = Auth.objects.get(id=payload.get('userId'))
                request.token_user = user  # important!
            except Auth.DoesNotExist:
                return JsonResponse({"message": "User not found"}, status=401)

        except (ValueError, jwt.ExpiredSignatureError, jwt.DecodeError) as e:
            return JsonResponse({"message": "Invalid or expired token", "error": str(e)}, status=401)

        return None

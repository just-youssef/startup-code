import firebase_admin 
from django.utils import timezone
from firebase_admin import auth, credentials
from rest_framework import authentication
from .exceptions import *
from .models import CustomUser

from pathlib import Path
fb_secret = Path(__file__).resolve().parent
cred = credentials.Certificate(fb_secret / "startup-727ee-firebase-adminsdk-bpzip-49815ad7ff.json")
default_app = firebase_admin.initialize_app(cred)


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")

        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()

        user, created = CustomUser.objects.get_or_create(uuid=uid)
        if created: user.username = f"user-{uid}"
        user.last_login = timezone.now()
        user.save()

        return (user, None)
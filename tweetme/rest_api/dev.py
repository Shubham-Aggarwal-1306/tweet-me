from rest_framework.authentication import BasicAuthentication
from django.contrib.auth import get_user_model


User = get_user_model()

class DevAuthentication(BasicAuthentication):
    def authenticate(self, request):
        qs = User.objects.filter(id=1)
        if qs.exists():
            return (qs.first(), None)
        return None
    


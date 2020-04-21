from .models import User
from rest_framework.parsers import JSONParser


def IsLoggedIn(request):
    if request.session.has_key("username"):
        try:
            user = User.objects.get(username=request.session["username"])
            return user

        except:
            return None
    else:
        return None
        
def IsRegistered(request):
    try:
        data = User.objects.get(roll=request.data['roll'])
        return data.activated
    except:
        return None

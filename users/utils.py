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

def IsFollowing(username, follow_username):
    user = User.objects.get(username=username)
    try:
        follow_user = user.following.get(username=follow_username)
    except:
        follow_user = None
    if follow_user is not None:
        return True
    else:
        return False

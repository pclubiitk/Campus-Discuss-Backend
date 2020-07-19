from .models import Stream
from users.models import User

def IsFollowing(username, pk):
    try:
        stream = Stream.objects.get(pk=pk)
        user = stream.followed_by.get(username=username)
        return True
    except:
        return False

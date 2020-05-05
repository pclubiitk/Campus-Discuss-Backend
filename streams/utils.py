from .models import Stream
from users.models import User

def IsFollowing(username, stream_title):
    try:
        stream = Stream.objects.get(title=stream_title)
        user = stream.followed_by.get(username=username)
        return True
    except:
        return False

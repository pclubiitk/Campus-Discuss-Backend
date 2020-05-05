from users.utils import IsLoggedIn
from rest_framework import status
from rest_framework.response import Response
from posts.models import Post
from bookmark.models import Bookmark
from rest_framework.views import APIView

class CreateAndDeleteBookmark(APIView):
    
    def post(self,request):
        try:
            pk = request.data['pk']
            try:
                post = Post.objects.get(pk=pk)
            except post.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            user = IsLoggedIn(request)
            if user is None:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            
            bookmark = Bookmark.objects.filter(user=user,post=post)
            if len(bookmark) != 0:
                bookmark.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                Bookmark.objects.create(user=user,post=post)
                return Response(status=status.HTTP_201_CREATED)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

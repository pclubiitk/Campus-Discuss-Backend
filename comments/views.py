from users.utils import IsLoggedIn
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from posts.models import Post
from .models import Comment

class CreateComment(APIView):

    def post(self,request):
        try:
            user=IsLoggedIn(request)
            if user is None:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            post_id=request.data['pk']
            content=request.data['content']
            try:
                post=Post.objects.get(pk=post_id)
            except post.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            try:
                parent_id=request.data['parent_id']
                parent_comment=Comment.objects.get(pk=parent_id)
                Comment.objects.create(user=user,content=content,post=post,parent=parent_comment)
                return Response(status=status.HTTP_200_OK)
            except: 
                Comment.objects.create(user=user,content=content,post=post)
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



def recursiveDelete(comment):
    sub_comments=Comment.objects.filter(parent=comment)
    if len(sub_comments) is not 0:
        for com in sub_comments:
            recursiveDelete(com)
    comment.delete()

class DeleteComment(APIView):
    
    def delete(self,request):
        try:
            user=IsLoggedIn(request)
            if user is None:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            

            comment_id=request.data['pk']
            try:
                comment=Comment.objects.get(pk=comment_id)
            except comment.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            
            if comment.user==user:
                recursiveDelete(comment)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)









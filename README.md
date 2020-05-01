# Campus-Discuss-Backend
## API Endpoints
A description of all the API endpoints, their URL and request parameters
### Users
#### Follow User
To follow another user.
```
url : /users/follow/
method : PUT
parameters = {"username" : "<username of the user to be followed>"}
```
#### Unfollow User
To unfollow a user who is already followed.
```
url : /users/unfollow/
method : DELETE
parameters = {"username" : "<username of the user to be unfollowed">}
```
### Posts
#### Create Post
To create a new post
```
url : /posts/create/
method : POST
parameters = {
    "title" : "<title of the post to be created>"
    "text" : "<contents of the post>"
    "stream" : "<title of the stream under which this post comes>"
}
```
#### Delete Post
Allows deletion of a post by its author.
```
url : /posts/delete/
method : DELETE
parameters = {"pk" : "<primary key of the post>}
```
### Streams
#### Follow Stream
To follow a stream.
```
url : /streams/follow/
method : PUT
parameters = {"title" : "<title of the stream to be followed>"}
```
#### Fetch Posts by Stream
To display posts corresponding to a stream
```
url : /streams/<int:pk>/posts/
method : GET
```

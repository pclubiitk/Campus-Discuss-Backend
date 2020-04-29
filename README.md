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
### Posts
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

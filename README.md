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
#### Create Post
To create a new post
```
url : /posts/create/
method : POST
parameters = {
    "post_title" : "<title of the post to be created>"
    "post_text" : "<contents of the post>"
    "stream_title" : "<title of the stream under which this post comes>"
}
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
url : /streams/<pk:id>/posts/
method : GET
```

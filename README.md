# Campus-Discuss-Backend
## API Endpoints
A description of all the API endpoints, their URL and request parameters.
### Users
#### Login
```
url : /users/auth/login/
method : POST
parameters = {
    "username" : "<username>",
    "password" : "<password>:
    }
```
#### Logout
```
url : /users/auth/logout/
method : POST
parameters = {}
```
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

#### Fetch Feed Posts
To see posts from followed users and streams
```
url : /users/feed/
method : GET
```

#### Fetch Posts by User
To display posts corresponding to a user
```
url : /users/<int:pk>/posts
method : GET
comments : pk in url is the primary key for user
```
### Posts
#### Create Post
To create a new post
```
url : /posts/create/
method : POST
parameters = {
    "title" : "<title of the post to be created>",
    "text" : "<contents of the post>",
    "stream" : "<title of the stream under which this post comes>"
}
```
#### Delete Post
Allows deletion of a post by its author.
```
url : /posts/delete/
method : DELETE
parameters = {"pk" : "<primary key of the post>"}
```
#### View Post
To see a post in detail
```
url : /posts/view/<int:pk>/
method : GET
```
#### Edit Post
Edit post if user is the author.
```
url : /posts/edit/
method : PUT
parameters = {
    "pk" : "<primary key of the post>",
    "title" : "<new title>",
    "text" : "<new content>"
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
#### Unfollow Stream
To unfollow a stream.
```
url : /streams/unfollow/
method : DELETE
parameters = {"title" : "<title of the stream to be unfollowed>"}
```
#### Fetch Posts by Stream
To display posts corresponding to a stream
```
url : /streams/<int:pk>/posts/
method : GET
```
### Bookmark
#### Bookmark/Unbookmark
To bookmark a post or to unbookmark already existing bookmark
```
url : /bookmarks/create/
method : POST
parameters = {"pk":"<primary key of the post>"}
```
### Comment
#### Create Comment
To comment on post or sub-comment on a comment
```
url : /comments/create/
method : POST
parameters = {
    "content" : "<content of comment>",
    "post_id" : "<primary key of the post>",
    "parent_id" : "<primary key of the parent comment">
}
comments : parent_id is not required if the comment is not a reply
```
#### Delete Comment
To delete a comment on a post(all sub-comments will be deleted)/delete sub-comments(all of its sub-comments will be deleted).Recursive deletion will be followed
```
url : /comments/delete
method : DELETE
parameters = {
    "pk":"<primary key of the comment>"
}
```

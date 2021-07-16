# Campus-Discuss-Backend
## API Endpoints
A description of all the API endpoints, their URL and request parameters.
### Users
#### View User
```
url : /users/profile/
method : GET

Successful : 200_OK
Unsuccessful : 404_BAD_REQUEST / 401_UNAUTHORIZED

Response : {
            "roll",
            "username",
            "name",
            "email",
            "fblink"
}

Note : User needs to be logged in to use this API.
```
#### Login
```
url : /users/auth/login/
method : POST
parameters = {
    "username" : "<username>",
    "password" : "<password>:
    }
```
```
Successful : 200_OK
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED
```
#### Logout
```
url : /users/auth/logout/
method : POST
parameters = {}
```
```
Successful : 200_OK
Unsuccessful : 401_UNAUTHORIZED
```
#### Follow User
To follow another user.
```
url : /users/follow/
method : PUT
parameters = {"username" : "<username of the user to be followed>"}
```
```
Successful : 200_OK
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED
```
#### Unfollow User
To unfollow a user who is already followed.
```
url : /users/unfollow/
method : POST
parameters = {"username" : "<username of the user to be unfollowed">}
```
```
Successful : 200_OK
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED
```
#### Fetch Feed Posts
To see posts from followed users and streams
```
url : /users/feed/
method : GET
```
```
Successful : {
                "post_title",
                "post_text",
                "pub_date",
                "last_modified",
                "author",
                "stream"
            }
Unsuccessful : 401_UNAUTHORIZED
```
#### Fetch Posts by User
To display posts corresponding to a user
```
url : /users/<int:pk>/posts
method : GET
comments : pk in url is the primary key for user
```
```
Successful : {
                [
                    {
                        "post_title",
                        "post_text",
                        "pub_date",
                        "last_modified",
                        "author",
                        "stream"
                    },
                ],
                "username"
            }
Unsuccessful : 404_NOT_FOUND
```
#### Fetch Posts by Bookmarks
To display posts corresponding to bookmarks of a loggedin user
```
url: /users/bookmarks/
method: GET
comments: the user must be logged in 
```
```
Successful : {
                "post_title",
                "post_text",
                "pub_date",
                "last_modified",
                "author",
                "stream"
            }
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED
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
```
Successful : 201_CREATED
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED
```
#### Delete Post
Allows deletion of a post by its author.
```
url : /posts/delete/
method : POST
parameters = {"pk" : "<primary key of the post>"}
```
```
Successful : 204_NO_CONTENT
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED
```
#### View Post
To see a post in detail
```
url : /posts/view/<int:pk>/
method : GET
```
```
Successful : {
                "pk",
                "post_title",
                "post_text",
                "pub_date",
                "last_modified",
                "author",
                "stream"
            }
Unsuccessful : 404_NOT_FOUND
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
```
Successful : 201_CREATED
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED
```
### Streams
#### Follow Stream
To follow a stream.
```
url : /streams/follow/
method : PUT
parameters = {"pk" : "<pk of the stream to be followed>"}
```
```
Successful : 200_OK
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED
```
#### Unfollow Stream
To unfollow a stream.
```
url : /streams/unfollow/
method : POST
parameters = {"pk" : "<pk of the stream to be unfollowed>"}
```
```
Successful : 200_OK
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED
```
#### Fetch Posts by Stream
To display posts corresponding to a stream
```
url : /streams/<int:pk>/posts/
method : GET
```
```
Successful : {
                "title",
                [
                    {
                        "post_title",
                        "post_text",
                        "pub_date",
                        "last_modified",
                        "author",
                        "stream"
                    },
                ]
            }
Unsuccessful : 404_NOT_FOUND
```
#### Fetch Subscribed Streams
Displays all the streams subscribed by the user.
```
url : /streams/subbed/
method : GET
```
```
Successful : [
    {
        "title",
        "description",
        "pk"
    },
]
200_OK
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED
```
#### Fetch all Streams
```
url : /streams/all/
method : GET
```
```
Successful : [
    {
        "title",
        "description",
        "pk",
        "is_subscribed"
    },
]
200_OK
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED
```
### Bookmark
#### Bookmark/Unbookmark
To bookmark a post or to unbookmark already existing bookmark
```
url : /bookmarks/create/
method : POST
parameters = {"pk":"<primary key of the post>"}
```
```
Successful : 201_CREATED / 204_NO_CONTENT
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED
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
```
Successful : {
        "pk",
        "parent",
        "post",
        "content",
        "created_at",
        "user"
        "replies": []
    }
200_OK
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED / 404_NOT_FOUND
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
```
Successful : 204_NO_CONTENT
Unsuccessful : 400_BAD_REQUEST / 401_UNAUTHORIZED / 404_NOT_FOUND
```
#### Fetch Comments by Post
View all the comments (and their replies) of a post recursively.
```
url: /comments/view/<int:pk>/
method : GET
```
pk = primary key of the post
```
Successful : [
    {
        "pk",
        "parent",
        "post",
        "content",
        "created_at",
        "user"
        "replies": [
            <comment>,
            <comment>
        ]
    },
]
Unsuccessful : 404_NOT_FOUND
```

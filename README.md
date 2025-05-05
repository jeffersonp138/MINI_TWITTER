

# Mini_Twitter API
Mini_Twitter is a RESTful API designed to provide core social media functionality. Built with Django and Django REST Framework, it allows users to register, authenticate, tweet, like tweets, follow other users, and view a personalized feed. This API is secure, scalable, and production-ready, using JWT for authentication and modular design for future enhancements.

## Features
*  User Registration & Authentication:

    * Register a new account with an email, username, and password.
    * Authenticate with JWT tokens for secure access.
    * Refresh token functionality to maintain session without re-authentication.

* Tweeting:

    * Create tweets with text, an image, or both.
    * View and interact with tweets, including a like/unlike option.
     
* User Following:

    * Follow or unfollow other users.
    * View tweets from followed users in a personalized feed.
* Personalized Feed:

   * See a feed of tweets from followed users, with support for pagination.
### Technologies Used:
* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL (configurable for other relational databases)
* **Authentication:** JWT (JSON Web Tokens) for secure user sessions
* **Storage:** Local storage for images 
* **Containerization:** Docker support for environment consistency





# API Endpoints
## Authentication:
- **POST /v1/users/register/:** Register a new user.
- **POST /v1/users/login/:** Authenticate and receive JWT tokens.
- **POST /v1/users/refresh/:** Refresh the access token.
## User Following:
- **POST /v1/users/follow/<username>/:** Follow a user.
- **POST /v1/users/unfollow/<username>/:** Unfollow a user.
## Tweeting:
- **POST /v1/tweets/:** Create, edit, delete a tweet.
- **POST /v1/tweets/like/<tweet_id>/:** Like or unlike a tweet.
- **GET /v1/tweets/<tweet_id>/:** Retrieve a specific tweet.
## Feed:
- **GET /v1/feed/:**  Retrieve the user’s personalized feed.

#### Usage Notes:
- **Authentication:** All modifying actions require an access token.
- **Pagination:** Supported on list endpoints, such as the feed.
- **Error Handling:** Standardized error responses with appropriate HTTP status codes.




##  Documentação: 

[Documentação](https://documenter.getpostman.com/view/39149693/2sAY4skQqb)

## Licença

[MIT](https://choosealicense.com/licenses/mit/)


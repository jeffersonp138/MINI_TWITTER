

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserRegisterView, CustomTokenObtainPairView
from .views import  TweetDetailView, CreateTweet, LikeTweet
from .views import FollowUser, UnfollowUser, UserFeed

urlpatterns = [
    path('users/register/', UserRegisterView.as_view(), name='user-register'),
    path('users/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/follow/<username>/', FollowUser.as_view(), name='follow_user'),
    path('users/unfollow/<username>/', UnfollowUser.as_view(), name='unfollow_user'),


    path('tweets/', CreateTweet.as_view(), name='create_tweet'),
    path('tweets/<int:tweet_id>/', TweetDetailView.as_view(), name='tweet_detail'), 
    path('tweets/like/<int:tweet_id>/', LikeTweet.as_view(), name='like_tweet'),


    path('feed/', UserFeed.as_view(), name='user_feed'),
]
#from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegisterSerializer, TweetSerializer
from .models import Tweet, User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404


# View para registro de usuário
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])  # Define a senha de forma segura
        user.save()

# View para login (obtenção do token)
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]



# Seguir/Deixar de seguir um usuário
class FollowUser(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request, username):
        user_to_follow = get_object_or_404(User, username=username)
        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        if request.user.following.filter(id=user_to_follow.id).exists():
            return Response(
                {"error": f"You are already following {username}."},
                status=status.HTTP_409_CONFLICT
            )
      
        request.user.following.add(user_to_follow)
        return Response({"status": f"You are now following {username}"})



class UnfollowUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, username):    
        user_to_unfollow = get_object_or_404(User, username=username)
        
        if request.user == user_to_unfollow:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if not request.user.following.filter(id=user_to_unfollow.id).exists():
            return Response(
                {"error": f"You are not following {username}."},
                status=status.HTTP_409_CONFLICT
            )
        # Remove the user from the following list
        request.user.following.remove(user_to_unfollow)
        return Response({'status': f'Stopped following {username}'}, status=status.HTTP_200_OK)

class CreateTweet(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   

class LikeTweet(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request, tweet_id):
        tweet = get_object_or_404(Tweet, id=tweet_id)

        if request.user in tweet.liked_by.all():
            tweet.liked_by.remove(request.user)
            return Response({"status": "You unliked this tweet"}, status=status.HTTP_200_OK)
        else:
            tweet.liked_by.add(request.user)
            return Response({"status": "You liked this tweet."})
    


class FeedPagination(PageNumberPagination):
    page_size = 10 # Defini a quantidade por página 
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserFeed(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TweetSerializer
    pagination_class = FeedPagination

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        queryset = Tweet.objects.filter(user__in=following_users).order_by('-created_at')
        return queryset


class TweetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        tweet = get_object_or_404(Tweet, id=self.kwargs['tweet_id'], user=self.request.user)
        return tweet
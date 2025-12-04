from django.urls import path
from .views import TweetPosts,GetUserPosts,getPostDetails,addComment,updateComment,deleteComment,likePost,deleteLike
import uuid 

urlpatterns = [
    path('', TweetPosts.as_view(), name='get_all_posts'),
    path('get-user-posts/', GetUserPosts.as_view(), name='get_user_posts'),
    path('post-details/<uuid:pk>/', getPostDetails, name='post-details'),
    path('add-comment/<uuid:pk>/', addComment, name='add-comment'),
    path('update-comment/<uuid:pk>/', updateComment, name='update-comment'),
    path('delete-comment/<uuid:pk>/', deleteComment, name='delete-comment'),
    path('like-post/<uuid:pk>/', likePost, name='like-post'),
    path('remove-like/<uuid:pk>/', deleteLike, name='remove-like'),
]

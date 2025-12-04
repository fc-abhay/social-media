from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Post, Comment, Like
from .serializer import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.response import Response
from rest_framework import status
from auths.pagination import CustomPagination
from rest_framework.views import APIView

# Create your views here.

class TweetPosts(APIView):
    
    def get(self, request):
        try:
            posts = Post.objects.all().order_by('-created_at')
            paginator = CustomPagination()
            paginated_posts = paginator.paginate_queryset(posts, request)

            serializer = PostSerializer(paginated_posts, many=True)

            # custom response
            return Response({
                "total_posts": posts.count(),
                "total_pages": paginator.page.paginator.num_pages,
                "current_page": paginator.page.number,
                "next": paginator.get_next_link(),
                "previous": paginator.get_previous_link(),
                "results": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error rendering all posts: {e}")
            return Response({"error": "Error fetching posts"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        try:
            data = {
                "content": request.data.get("content"),
                "createdBy_id": request.token_user.id
            }

            serializer = PostSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(f"Error creating post: {e}")
            return Response({"error": "Error creating post"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def patch(self, request):
        try:
            post_id = request.data.get("post_id")
            content = request.data.get("content")
            
            post = Post.objects.filter(id=post_id).first()
            if not post:
                return Response({"error": "Post not found or unauthorized"}, status=status.HTTP_404_NOT_FOUND)
            
            if not post.createdBy == request.token_user.id:
                return Response({"error": "Unauthorized to edit this post"}, status=status.HTTP_403_FORBIDDEN)

            post.content = content
            post.createdBy_id = request.token_user.id
            post.save()

            serializer = PostSerializer(post)
            return Response(
                {
                    "message": "Post updated successfully",
                    "post": serializer.data
                }, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error in PATCH method: {e}")
            return Response({"error": "Error processing request"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request):
        try:
            post_id = request.data.get("post_id")
            post = Post.objects.filter(id=post_id).first()
            if not post:
                return Response({"error": "Post not found or unauthorized"}, status=status.HTTP_404_NOT_FOUND)

            post.delete()
            return Response({"message": "Post deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error deleting post: {e}")
            return Response({"error": "Error processing request"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class GetUserPosts(APIView):
    def get(self, request):
        try:
            user = request.token_user
            posts = Post.objects.filter(createdBy=user).order_by('-created_at')
            paginator = CustomPagination()
            paginated_posts = paginator.paginate_queryset(posts, request)

            serializer = PostSerializer(paginated_posts, many=True)

            # custom response
            return Response({
                "total_posts": posts.count(),
                "total_pages": paginator.page.paginator.num_pages,
                "current_page": paginator.page.number,
                "next": paginator.get_next_link(),
                "previous": paginator.get_previous_link(),
                "results": serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error rendering user posts: {e}")
            return Response({"error": "Error fetching user posts"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(["GET"])
def getPostDetails(request, pk):
    try:
        post = Post.objects.filter(id=pk).first()

        if not post:
            return Response(
                {"error": "Post not found!!!"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PostSerializer(post)

        return Response(
            {"results": serializer.data},
            status=status.HTTP_200_OK
        )

    except Exception as e:
        print("Error:", e)
        return Response(
            {"error": "Error fetching user posts"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["POST"])
def addComment(request,pk):
    try:
        post = Post.objects.filter(id=pk).first()
        if not post:
            return Response(
                {"error": "Post not found!!!"},
                status=status.HTTP_404_NOT_FOUND
            )

        data={
            "content":request.data.get("content"),
            "createdBy":request.token_user.id,
            "post":pk
        }
        addNewComment= CommentSerializer(data=data)
        if addNewComment.is_valid():
            addNewComment.save()
            return Response(addNewComment.data, status=status.HTTP_201_CREATED)

        return Response(addNewComment.errors, status=status.HTTP_400_BAD_REQUEST)
            
    except Exception as e:
        print("Error:", e)
        return Response(
            {"error": "Error fetching user posts"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
@api_view(["PATCH"])
def updateComment(request, pk):
    try:
        # Find the comment by ID + only allow the owner
        comment = Comment.objects.filter(
            id=pk,
            createdBy=request.token_user.id
        ).first()
        
        print(comment)

        if not comment:
            return Response(
                {"error": "Comment not found or unauthorized"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Update content
        new_content = request.data.get("content")
        if not new_content:
            return Response(
                {"error": "content is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        comment.content = new_content
        comment.save()

        # Serialize updated comment
        serializer = CommentSerializer(comment)

        return Response(
            {
                "message": "Comment updated successfully",
                "comment": serializer.data
            },
            status=status.HTTP_200_OK
        )

    except Exception as e:
        print("Error:", e)
        return Response(
            {"error": "Error updating comment"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
@api_view(["DELETE"])
def deleteComment(request, pk):
    try:
        # Find the comment by ID + only allow the owner
        comment = Comment.objects.filter(
            id=pk,
            createdBy=request.token_user.id
        ).first()
        
        if not comment:
            return Response(
                {"error": "Comment not found or unauthorized"},
                status=status.HTTP_404_NOT_FOUND
            )

        comment.delete()

        return Response(
            {
                "message": "Comment deleted successfully",
            },
            status=status.HTTP_200_OK
        )

    except Exception as e:
        print("Error:", e)
        return Response(
            {"error": "Error updating comment"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        

@api_view(["POST"])
def likePost(request,pk):
    try:
        post = Post.objects.filter(id=pk).first()
        if not post:
            return Response(
                {"error": "Post not found!!!"},
                status=status.HTTP_404_NOT_FOUND
            )
        data={
            "createdBy":request.token_user.id,
            "post":pk
        }
        addNewLike= LikeSerializer(data=data)
        if addNewLike.is_valid():
            addNewLike.save()
            return Response(addNewLike.data, status=status.HTTP_201_CREATED)

        return Response(addNewLike.errors, status=status.HTTP_400_BAD_REQUEST)
            
    except Exception as e:
        print("Error:", e)
        return Response(
            {"error": "Error fetching user posts"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
        
@api_view(["DELETE"])
def deleteLike(request, pk):
    try:
        # Find the comment by ID + only allow the owner
        like = Like.objects.filter(
            id=pk,
            createdBy=request.token_user.id
        ).first()
        
        if not like:
            return Response(
                {"error": "Like not found or unauthorized"},
                status=status.HTTP_404_NOT_FOUND
            )

        like.delete()

        return Response(
            {
                "message": "Like deleted successfully",
            },
            status=status.HTTP_200_OK
        )

    except Exception as e:
        print("Error:", e)
        return Response(
            {"error": "Error updating comment"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

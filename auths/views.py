from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from posts.serializer import PostSerializer
from .models import Auth
from django.contrib.auth.hashers import check_password
import jwt
from datetime import datetime, timedelta
from django.conf import settings



SECRET_KEY = settings.SECRET_KEY or "twitterbackendsecrete"


@api_view(["POST"])
def registerView(request):
    username = request.data.get("username")
    fullName = request.data.get("fullName")
    email = request.data.get("email")
    password = request.data.get("password")
    
    # Validate required fields
    if not username or not password or not email or not fullName:
        return Response(
            {"error": "All fields are required!!!"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Correct payload
    payload = {
        "username": username,
        "fullName": fullName,
        "email": email,
        "password": password
    }

    serializer = UserSerializer(data=payload)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "User added successfully!!!",
                "status": "success",
                "user": serializer.data,
            },
            status=status.HTTP_201_CREATED
        )

    errors = serializer.errors

    # Custom readable message
    message = ""

    if "username" in errors:
        message = "Username already exists."
    elif "email" in errors:
        message = "Email already registered."
    else:
        message = "Invalid data."

    return Response(
        {
            "status": "error",
            "message": message,
            # "details": errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
def loginView(request):
    try:
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({
                "message": "Username and password are required",
                "status": "error"
            }, status=status.HTTP_400_BAD_REQUEST)

        user = Auth.objects.filter(username=username).first()
        if user and check_password(password, user.password):
            # TODO: Generate JWT token here
            payload={
                "userId":str(user.id),
                "exp": datetime.utcnow() + timedelta(days=30) 
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

            return Response({
                "message": "User logged in successfully!",
                "status": "success",
                "token": token
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "message": "Username or password is invalid!",
                "status": "error"
            }, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response({
            "message": "An error occurred during login",
            "status": "error",
            "details": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
@api_view(["GET"])
def getUserDetails(request):
    try:
        user = request.token_user
        posts = user.posts.all()  # Queryset of posts
        posts_serialized = PostSerializer(posts, many=True).data
        user_data = {
            "id": str(user.id),  # if it's UUID
            "username": user.username,
            "email": user.email,
            "posts": posts_serialized,
            # add more fields if needed
        }

        return Response({
            "message": "User details fetched successfully",
            "user": user_data,
            "status": "success",
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "An error occurred during login",
            "status": "error",
            # "details": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(["GET"])
def getOtherUserInfo(request,pk):
    print("here")
    try:
        user = Auth.objects.filter(id=pk).first()
        if not user:
            return Response({
                "message": "User not found",
                "status": "error",
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response({
            "message": "User details fetched successfully",
            "user": serializer.data,
            "status": "success",
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "An error occurred while fetching user details",
            "status": "error",
            # "details": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(["PUT"])
def updateProfileView(request):
    try:
        user_id = request.token_user.get("id") if isinstance(request.token_user, dict) else request.token_user.id
        user = Auth.objects.filter(id=user_id).first()
        
        if not user:
            return Response({
                "message": "User not found",
                "status": "error",
            }, status=status.HTTP_404_NOT_FOUND)

        fullName = request.data.get("fullName")
        password = request.data.get("password")

        payload = {}

        if fullName:
            payload["fullName"] = fullName

        if password:
            payload["password"] = password

        serializer = UserSerializer(instance=user, data=payload, partial=True)

        if not serializer.is_valid():
            return Response({
                "message": "Invalid data",
                "errors": serializer.errors,
                "status": "error",
            }, status=status.HTTP_400_BAD_REQUEST)

        # IMPORTANT: NEVER assign serializer.save() result to serializer
        updated_user = serializer.save()     # this returns instance

        return Response({
            "message": "Profile updated successfully",
            "user": UserSerializer(updated_user).data,   # fresh serializer
            "status": "success",
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "message": "An error occurred while updating profile",
            "status": "error",
            "details": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def deleteUserView(request):
    try:
        user_id = request.token_user.get("id") if isinstance(request.token_user, dict) else request.token_user.id
        user = Auth.objects.filter(id=user_id).first()
        
        if not user:
            return Response({
                "message": "User not found",
                "status": "error",
            }, status=status.HTTP_404_NOT_FOUND)

        user.delete()

        return Response({
            "message": "User deleted successfully",
            "status": "success",
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "message": "An error occurred while deleting user",
            "status": "error",
            "details": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

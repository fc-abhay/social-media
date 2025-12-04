from rest_framework import serializers
from .models import Auth
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True}
        }

    # Create user → hash password
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    # Update user → hash password if password exists in update
    def update(self, instance, validated_data):
        password = validated_data.get("password", None)

        if password:
            validated_data["password"] = make_password(password)

        return super().update(instance, validated_data)

from rest_framework import serializers
from .models import Auth
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    # Case-insensitive uniqueness validation for username
    def validate_username(self, value):
        if Auth.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    # Case-insensitive uniqueness validation for email
    def validate_email(self, value):
        if Auth.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email already registered.")
        return value

    # Hash password on create
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    # Hash password on update
    def update(self, instance, validated_data):
        password = validated_data.get("password", None)
        if password:
            validated_data["password"] = make_password(password)
        return super().update(instance, validated_data)

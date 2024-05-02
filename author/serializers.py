from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    pseudonym = serializers.CharField(allow_blank=True,
                                      allow_null=True)
    age = serializers.IntegerField()
    retired = serializers.BooleanField()

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data("first_name", instance.first_name)
        instance.last_name = validated_data("last_name", instance.last_name)
        instance.pseudonym = validated_data("pseudonym", instance.pseudonym)
        instance.age = validated_data("age", instance.age)
        instance.retired = validated_data("retired", instance.retired)
        instance.save()
        return instance

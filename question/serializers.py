from rest_framework import serializers
from question.models import Question

class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    text = serializers.CharField()
    added_at = serializers.DateTimeField()
    rating = serializers.IntegerField()
    tags = serializers.ListField(source='get_tags')

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.text = validated_data.get('text', instance.text)
        instance.added_at = validated_data.get('added_at', instance.added_at)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.save()
        return instance
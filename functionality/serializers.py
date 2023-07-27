from rest_framework import serializers
from .models import User, Question, FavoriteQuestion, ReadQuestion

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['idname', 'display_name', 'email', 'phone']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id', 'question', 'option1', 'option2', 'option3', 
            'option4', 'option5', 'answer', 'explain'
        ]

class FavoriteQuestionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = FavoriteQuestion
        fields = ['user', 'question']

class ReadQuestionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = ReadQuestion
        fields = ['user', 'question']

# Inside functionality/tests.py

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import User, Question, FavoriteQuestion, ReadQuestion
from .serializers import UserSerializer, QuestionSerializer

class ModelCreationTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            idname="testuser",
            display_name="Test User",
            email="testuser@example.com",
            phone="1234567890"
        )
        self.question = Question.objects.create(
            question="Sample Question?",
            option1="Option 1",
            option2="Option 2",
            option3="Option 3",
            option4="Option 4",
            option5="Option 5",
            answer=1,
            explain="Explanation for the question."
        )

    def test_user_creation(self):
        user = User.objects.get(idname="testuser")
        self.assertEqual(user.display_name, "Test User")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.phone, "1234567890")

    def test_question_creation(self):
        question = Question.objects.get(question="Sample Question?")
        self.assertEqual(question.option1, "Option 1")
        self.assertEqual(question.answer, 1)

class UserStatsAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            idname="testuserapi",
            display_name="Test User API",
            email="testuserapi@example.com",
            phone="9876543210"
        )
        self.url = reverse('user-stats')

    def test_user_stats_retrieval(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if our user is in the response
        user_exists = any(item for item in response.data if item['user_id'] == self.user.id)
        self.assertTrue(user_exists)

class FilterQuestionsAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            idname="testuserapi2",
            display_name="Test User API 2",
            email="testuserapi2@example.com",
            phone="9876543211"
        )
        self.question = Question.objects.create(
            question="Another Sample Question?",
            option1="Option 1",
            option2="Option 2",
            option3="Option 3",
            option4="Option 4",
            option5="Option 5",
            answer=1,
            explain="Explanation for the question."
        )
        self.url = reverse('filter-questions')

    def test_filter_questions(self):
        response = self.client.get(self.url, {'user_id': self.user.id, 'status': 'unread'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify the question is in the response since it is unread by the user
        question_exists = any(item['id'] == self.question.id for item in response.data)
        self.assertTrue(question_exists)


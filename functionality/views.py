from django.http import JsonResponse
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Question, FavoriteQuestion, ReadQuestion
from .serializers import UserSerializer, QuestionSerializer

@api_view(['GET'])
def user_stats(request):
    users = User.objects.all()
    paginator = Paginator(users, 100)

    page_num = request.GET.get('page', 1)
    page = paginator.page(page_num)
    
    data = []

    for user in page.object_list:
        fav_count = FavoriteQuestion.objects.filter(user=user).count()
        read_count = ReadQuestion.objects.filter(user=user).count()
        user_data = {
            'user_id': user.id,
            'favorite_count': fav_count,
            'read_count': read_count
        }
        data.append(user_data)

    return Response(data)  # Using DRF's Response for consistent JSON responses

@api_view(['GET'])
def filter_questions(request):
    user_id = request.GET.get('user_id')
    status = request.GET.get('status')  # ["read", "unread", "favorite", "unfavorite"]

    # Assuming user_id is mandatory for this view
    if not user_id:
        return Response({'error': 'user_id parameter required'}, status=400)

    user = User.objects.get(pk=user_id)
    
    # Query according to the given status
    if status == "read":
        read_questions = ReadQuestion.objects.filter(user=user)
        questions = Question.objects.filter(id__in=read_questions.values_list('question_id', flat=True))
    elif status == "unread":
        read_questions = ReadQuestion.objects.filter(user=user)
        questions = Question.objects.exclude(id__in=read_questions.values_list('question_id', flat=True))
    elif status == "favorite":
        fav_questions = FavoriteQuestion.objects.filter(user=user)
        questions = Question.objects.filter(id__in=fav_questions.values_list('question_id', flat=True))
    elif status == "unfavorite":
        fav_questions = FavoriteQuestion.objects.filter(user=user)
        questions = Question.objects.exclude(id__in=fav_questions.values_list('question_id', flat=True))
    else:
        return Response({'error': 'Invalid status parameter'}, status=400)

    # Serialize the questions using the QuestionSerializer
    serializer = QuestionSerializer(questions, many=True)

    return Response(serializer.data)


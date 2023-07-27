from django.core.management.base import BaseCommand
from functionality.models import User, Question, FavoriteQuestion, ReadQuestion
import random
import string
from lorem import sentence, text
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Generates random user and question data'

    def generate_random_user(self):
        idname = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        display_name = f"User {idname}"
        email = f"{idname}@example.com"
        phone = ''.join(random.choices(string.digits, k=10))
        return User(idname=idname, display_name=display_name, email=email, phone=phone)

    def generate_random_question(self):
        question_text = sentence()
        options = [sentence() for _ in range(5)]
        answer = random.randint(1, 5)
        explanation = text()
        return Question(
            question=question_text,
            option1=options[0],
            option2=options[1],
            option3=options[2],
            option4=options[3],
            option5=options[4],
            answer=answer,
            explain=explanation
        )

    def handle(self, *args, **kwargs):
        num_users = 10_000_000
        num_questions = 1_000_000
        batch_size = 5000

        # Generate 10M users
        users_to_create = []
        for _ in tqdm(range(num_users), desc="Generating users"):
            users_to_create.append(self.generate_random_user())
            if len(users_to_create) == batch_size:
                User.objects.bulk_create(users_to_create)
                users_to_create = []

        # Remaining users (if not a multiple of batch_size)
        if users_to_create:
            User.objects.bulk_create(users_to_create)

        # Generate 1M questions
        questions_to_create = []
        for _ in tqdm(range(num_questions), desc="Generating questions"):
            questions_to_create.append(self.generate_random_question())
            if len(questions_to_create) == batch_size:
                Question.objects.bulk_create(questions_to_create)
                questions_to_create = []

        # Remaining questions (if not a multiple of batch_size)
        if questions_to_create:
            Question.objects.bulk_create(questions_to_create)

        # Create random FavoriteQuestion and ReadQuestion entries
        all_users = list(User.objects.all())
        all_questions = list(Question.objects.all())

        for _ in tqdm(range(num_questions), desc="Generating favorite and read entries"):
            random_user = random.choice(all_users)
            random_question = random.choice(all_questions)
            
            FavoriteQuestion.objects.get_or_create(user=random_user, question=random_question)
            ReadQuestion.objects.get_or_create(user=random_user, question=random_question)

        self.stdout.write(self.style.SUCCESS('Successfully generated random data'))

from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()

# Create your tests here.

class ReviewModelTest(TestCase):
    def setUp(self):
        # 테스트에 사용할 초기 데이터 생성
        self.user = User.objects.create(
            author='joy',
            content=' good place ',
            rating=5
        )

    def test_create_review(self):
        review = User.objects.get(author="joy")
        self.assertEqual(review.content, "good place ")
        self.assertEqual(review.rating, 5)
        self.assertIsNotNone(review.created_at)
        self.assertEqual(str(review), "joy - 5")
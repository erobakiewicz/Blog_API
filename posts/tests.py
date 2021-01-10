from django.contrib.auth.models import User
from django.test import TestCase

from posts.models import Post


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # creates test user
        testuser1 = User.objects.create_user(
            username="testuser1", password="1234"
        )
        testuser1.save()
        # creates test post
        test_post = Post.objects.create(
            author=testuser1, title='Post title', body='Body content'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Post title')
        self.assertEqual(body, 'Body content')

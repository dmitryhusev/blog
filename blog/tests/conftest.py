import pytest
from django.contrib.auth import get_user_model
from blog.models import Post


@pytest.fixture
def new_user(db):
    user = get_user_model().objects.create_user(
        username="testuser1", 
        email="hello@email.com",
        password="123")
    yield user
    
@pytest.fixture()
def new_post(db, new_user):
    post = Post.objects.create(
        title="A good title",
        body="Nice body content",
        author=new_user)
    return post

@pytest.fixture
def db_client(db, client):
    yield client
    
from django.urls import reverse
from blog.models import Post


def test_post_model(new_post):
    assert new_post.title == "A good title"
    assert new_post.body == "Nice body content"
    assert new_post.author.username == "testuser1"
    assert str(new_post) == "A good title"
    assert new_post.get_absolute_url() == "/post/1/"

def test_url_exists_at_correct_location_listview(db_client):
    response = db_client.get("/")
    assert response.status_code == 200

def test_url_exists_at_correct_location_detailview(new_post, db_client):
    response = db_client.get(f"/post/{new_post.id}/")
    assert response.status_code == 200

def test_post_listview(new_post, db_client):
    response = db_client.get(reverse("home"))
    assert response.status_code == 200
    assert new_post.body == "Nice body content"
    assert "home.html" in response.template_name

def test_post_detailview(new_post, db_client):
    response = db_client.get(reverse("post_detail", kwargs={"pk": new_post.pk}))
    no_response = db_client.get("/post/100000/")
    assert response.status_code == 200
    assert no_response.status_code == 404
    assert "post_detail.html" in response.template_name

def test_post_create(db_client, new_user):
    data = {
        'title': "A good title",
        'body': "Nice body content",
        'author': new_user.id
    }
    res = db_client.post('/post/new/', data=data)
    post = Post.objects.last()
    assert res.status_code == 302
    assert post.title == data['title']
    assert post.body == data['body']

def test_post_update(new_post, db_client):
    data = {
        'title': 'new title',
        'body': 'new body'
    }
    res = db_client.post(reverse('post_edit', args=str(new_post.id)), data=data)
    assert res.status_code == 302
    post = Post.objects.last()
    assert post.title == data['title']
    assert post.body == data['body']

def test_delete_post(new_post, db_client):
    assert new_post.title
    res = db_client.post(reverse('post_delete', args=str(new_post.id)))
    assert res.status_code == 302
    post = Post.objects.last()
    assert post == None

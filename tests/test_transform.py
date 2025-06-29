from app.transform import join_users_posts

def test_join_users_posts():
    users = [{"id": 1, "name": "Alice", "email": "alice@test.com"}]
    posts = [{"id": 10, "userId": 1, "title": "Test Post", "body": "Hello"}]

    df = join_users_posts(users, posts)

    assert not df.empty
    assert df.iloc[0]["PostTitle"] == "Test Post"
    assert df.iloc[0]["UserName"] == "Alice"

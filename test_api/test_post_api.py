# Module Import
from unittest import TestCase
from unittest.mock import patch

# Local Import
from main import PostAPI


class TestPostAPI(TestCase):
    def test_post_api_success(self):
        api = PostAPI()
        with patch("requests.sessions.Session.get") as mock_get_posts:
            mock_get_posts.return_value.json.return_value = self.mock_post_data()
            response = api.get_posts()

        for post in response:
            print(post)
            # self.assertIn(post, self.mock_post_data())
        self.assertTrue(False)

    @staticmethod
    def mock_post_data():
        return [{
            "userId": _id,
            "id": _id,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        } for _id in range(10)]

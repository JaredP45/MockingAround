# Module Import
from unittest import TestCase
from unittest.mock import patch

# Local Import
from main import JsonPlaceHolderThing
from requests import HTTPError


class TestPostAPI(TestCase):
    def test_post_api_success(self):
        """ Test if request call is successful and if response data is as expected """
        api = JsonPlaceHolderThing()
        with patch("requests.sessions.Session.get") as mock_get_posts:
            mock_get_posts.return_value.json.return_value = self.mock_post_data()
            response = api.get_posts()

        mock_get_posts.assert_called()
        for post in response:
            self.assertIn(post, self.mock_post_data())

    def test_post_api_fail(self):
        """ Test if request properly raises exception after request fail and if response is None """
        api = JsonPlaceHolderThing()
        error_message = str({"status": 404, "message": "Bad Request"})
        with patch("requests.sessions.Session.get") as mock_get_posts:
            mock_get_posts.side_effect = HTTPError(str(error_message))
            with self.assertRaises(Exception) as exc:
                response = api.get_posts()

                self.assertIsNone(response)
        mock_get_posts.assert_called_once()
        self.assertIn(error_message, str(exc.exception))

    @staticmethod
    def mock_post_data():
        return [{
            "userId": _id,
            "id": _id,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        } for _id in range(10)]

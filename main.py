import requests


class PostAPI:
    def __init__(self):
        self.session = requests.Session
        self.BASE_URL = "https://jsonplaceholder.typicode.com/"

    def get_posts(self):
        try:
            url = f"{self.BASE_URL}/posts"
            response = self.session.get(url=url)
            response.raise_for_status()
            for post in response:
                yield post
        except Exception as err:
            raise Exception(f"Unable to retrieve posts: {err}")

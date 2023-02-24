import requests


class JsonPlaceHolderThing:
    def __init__(self):
        self.BASE_URL = "https://jsonplaceholder.typicode.com"
        self.session = requests.Session()

    def get_posts(self):
        try:
            url = f"{self.BASE_URL}/posts"
            response = self.session.get(url=url)
            response.raise_for_status()
            return response.json()
        except Exception as err:
            raise Exception(f"Unable to retrieve posts: {err}")

if __name__ == '__main__':
    JsonPlaceHolderThing()

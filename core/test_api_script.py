import requests


class Request:
    def __init__(self, endpoint):
        self.domain = 'http://wezapps.work:8000'
        self.endpoint = endpoint
        self.url = self.domain + self.endpoint

    def get(self):
        return requests.get(self.url)

    def post(self, data):
        response = requests.post(self.url, data=data)
        return response

    def put(self, data):
        response = requests.put(self.url, data=data)
        return response

    def delete(self):
        response = requests.delete(self.url)
        return response


if __name__ == "__main__":
    api_endpoint = '/test-api1/8/'
    request = Request(api_endpoint)
    post_data_api1 = {
        "node": "new string again updated",
        "volume": 10
    }
    post_data_api2 = {
        "node": "new node",
        "isOn": True
    }
    # response = request.get()
    # response = request.post(data=post_data_api1)
    # response = request.put(data=post_data_api1)
    response = request.delete()
    print(f"status code: {response.status_code}")


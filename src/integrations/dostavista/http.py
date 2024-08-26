from settings import settings


class HTTP:
    def __init__(self):
        self.url = "https://robotapitest.dostavista.ru/api/business/1.5"
        self.token = settings.dostavista.token

    def get(self):
        ...

    def post(self):
        ...


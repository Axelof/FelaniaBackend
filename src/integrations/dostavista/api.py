from integrations.dostavista.http import HTTP


class API(HTTP):
    def __init__(self):
        super().__init__()

    def calculate_order(self):
        ...

    def create_order(self):
        ...

    def cancel_order(self):
        ...

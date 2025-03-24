class UserController:
    def __init__(self):
        pass

    def create_user(self): ...

    def read_user(self, **kwargs):
        print("-" * 40)
        print("Hola, Mundo!")
        print("-" * 40)
        return {"message": "Hola"}, 200

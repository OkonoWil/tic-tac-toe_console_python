class Player:
    def __init__(self, name: str = "", num: int = 1, token: str = ""):
        self.name = name
        self.num = num
        self.token = token

    def print_welcome_statement(self) -> None:
        print(f"Welcome! Player {self.num}, {self.name}, token: {self.token}\n")

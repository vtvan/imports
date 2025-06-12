class Cat:
    def __init__(self, name:str):
        self.name = name
    def show_name(self) -> str:
        return self.name

def say_hello(name:str) -> None:
    print(f'Hello, {name}')

my_name = '大貓'

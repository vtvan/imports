class ClientInformation:
    name = 'Oliver'
    age = 33

    def __init__(self):
        ...
    def greet(self):   # instance method
        print('Hello, world')
    def show_client_info(self):   # instance method
        print(f'{self.name=}\t{self.age=}')



def client_information() -> None:
    print('function client_information')


client_name = 'Alex'

# xyz = 35
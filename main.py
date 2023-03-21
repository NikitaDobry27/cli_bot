import re



contacts = {}


def input_error():
    pass

def input_formatter(str):
    words_from_string = re.findall(r'\b\w+\b', str)
    command = words_from_string[0]
    if len(words_from_string) == 1:
        return command, ''
    data = words_from_string[1:]
    return command, data


def command_parser(command):
    for func, word in COMMANDS.items():
        if command in word:
            return func


def hello(*args, **kwargs):
    return 'Hi! How can I help you'

def add_contact(*args, **kwargs):
    pass

def change(*args, **kwargs):
    pass

def phone(*args, **kwargs):
    pass

def show_all(*args, **kwargs):
    pass

def close(*args, **kwargs):
    pass

COMMANDS = {
        hello: ['hi', 'hello', 'hey'],
        add_contact: ['add']
    }

def main():
    while True:
        user_input = input('Type your query >>> ').lower()
        
        if user_input == 'close':
            print('See you!')
            return False
        
        call, data = input_formatter(user_input)

        command = command_parser(call)
        
        if command:
            print(command(data))
        

    # add_contact(user_input)
    # print(contacts)

if __name__ == "__main__":
    main()
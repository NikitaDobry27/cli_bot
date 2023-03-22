import re



contacts = {}

def input_validation(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return 'Please provide name and phone number'
        except TypeError:
            return f"{args[0]} is not a valid command"

    return wrapper


def input_formatter(str):
    words_from_string = re.findall(r'\b\w+\b', str)
    command = words_from_string[0]
    if len(words_from_string) == 1:
        return command, ''
    data = words_from_string[1:]
    return command, data

@input_validation
def command_handler(command):
    for func, word in COMMANDS.items():
        if command in word:
            return func
    return lambda x: f"{command} is not a valid command"

@input_validation
def hello(*args, **kwargs):
    return 'Hi! How can I help you'

@input_validation
def add_contact(*args, **kwargs):
    lst = args[0]
    name = lst[0]
    phone =lst[1]  
    
    if len(lst) < 2:
        return 'name or phone number is missing'
    if len(phone) > 15 or len(phone) < 9:
        return f'{phone} is not valid'
    contacts[name] = phone
    return 'Contact successfully added'


@input_validation
def change(*args, **kwargs):
    lst = args[0]
    name = lst[0]
    phone = lst[1]
    
    if name in contacts.keys():
        contacts[name] = phone
        return f'Phone number for contact {name} was successfully changed'

    else:
        return f'There is no such contact with name {name}'


@input_validation
def phone(*args, **kwargs):
    pass



def show_all(*args, **kwargs):
    if not contacts:
        return 'Your contacts list is empty'
    result = ''
    for k, v in contacts.items():
        result += f'\n{k.capitalize()}: {v}\n'
    return result

COMMANDS = {
        hello: ['hi', 'hello', 'hey'],
        add_contact: ['add'],
        change: ['change'],
        phone: ['phone'],
        show_all: ['show']
    }


def main():
    while True:
        user_input = input('Type your query >>> ').lower()
        
        if user_input == 'close':
            print('See you!')
            return False
        
        command, data = input_formatter(user_input)

        call = command_handler(command)
        
        
        print(call(data))
        

    # add_contact(user_input)
    # print(contacts)

if __name__ == "__main__":
    main()
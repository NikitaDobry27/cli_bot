

contacts = {}



def hello(str):
    return 'Hi! How can I help you'

def add_contact(str):
  
    formatted_str = str.split()
    if 'add' == formatted_str[0]:
        name = formatted_str[1]
        contacts[name] = formatted_str[2]

def main():
    user_input = input('Type your query >>> ')
    add_contact(user_input)
    print(contacts)

if __name__ == "__main__":
    main()
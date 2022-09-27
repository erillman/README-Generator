import os
from random import randint


def main():
    save_path = 'C:\\Users\Eric\Desktop\Learning Python\Text Files\README.md'
    bool_return = find_duplicate(save_path)
    if bool_return == True:
        new_name = ''
        _ = create_alphabet_list()
        for i in range(6):
            new_name += _[randint(0, 26)]
        new_path = f'C:\\Users\Eric\Desktop\Learning Python\Text Files\{new_name}.md'
        os.rename(save_path, new_name)
        create_new_file(save_path)
    else:
        create_new_file(save_path)


def create_new_file(og_path):
    h_bold = '# '
    sub_bold = '## '
    h1 = input('What would like you to name this program? ')
    des = input('What does this program do? ')
    use = input('How do you you use this program? ')
    title = format(f'{h_bold}{h1}\n')  # make this dynamic later
    desc = format(f'{sub_bold}Description:\n{des}')
    use = format(f'{sub_bold}How to use:\n{use}')
    output = title+'\n'+'\n'+desc+'\n'+'\n'+use

    new_file = open(og_path, 'w')
    new_file.write(output)
    new_file.close()


def create_alphabet_list():
    a_list = []
    a = 'a'
    for i in range(0, 26):
        a_list.append(a)
        a = chr(ord(a)+1)
    return a_list


def find_duplicate(path):
    if os.path.isfile(path) == True:
        x = True
    else:
        x = False
    return x


main()

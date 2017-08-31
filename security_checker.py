usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_name = input("please enter your username: ")
if user_name not in usernames:
    print("Access Denied")
else:
    print("Access granted")


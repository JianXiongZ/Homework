# encoding: utf-8
users = []
while True:
    command = input('Please input find/list/add/delete/update/exit: ')
    if command.strip() == 'add':
        is_bool = True
        user_info = input('Please input like name:age:tel style: ')
        name, age, tel = user_info.strip().split(':')
        # 可以这样使用a,b,c=[1,2,3]
        for user in users:
            if name == user['name']:
                print(name, ' is exited')
                is_bool = False
        if is_bool:
            users.append({'name': name, 'age': age, 'tel': tel})
            print(name, ' is added!')
    if command.strip() == 'delete':
        is_bool = True
        name = input('Please input a name: ')
        for user in users:
            if user['name'] == name.strip():
                users.remove(user)
                print ('user is deleted')
                is_bool = False
        if is_bool:
            print ('This\'s name is not exit.')
    if command.strip() == 'find':
        is_bool = True
        name = input('Please input a name: ')
        for user in users:
            if user['name'] == name.strip():
                i = list(user.values())
                print ('|{:<10}|{:<10}|{:<10}'.format('user', 'age', 'tel'))
                print ('|{0:<10}|{1:<10}|{2:<10}|'.format(i[0], i[1], i[2]))
                is_bool = False
        if is_bool:
            print('The name is not exit.')
    if command.strip() == 'exit':
        print ('exit now')
        break
    if command.strip() == 'list':
        print ('|{0:<10}|{1:<10}|{2:<10}|'.format('user', 'age', 'tel'))
        for user in users:
            print ('|{0:<10}|{1:<10}|{2:<10}|'.format(user['name'], user['age'], user['tel']))
    if command.strip() == 'update':
        is_bool = True
        user_info = input('Please input name:age:tel style : ')
        name, age, tel = user_info
        for user in users:
            if name not in user.values():
                print('user is not exit')
                is_bool = False
        if is_bool:
            user.update({'age': age, 'tel': tel})
            print('update succeed')

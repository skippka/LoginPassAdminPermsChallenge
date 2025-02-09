
# panel mini game (login and pass pc panels)

import getpass

class Perms:
    rights = {
        0: "Узнать баланс",
        1: "Выдать себе права",
        2: "Забрать у себя права",
        3: "Узнать свои права",
        4: "Информация",
        5: "Выход"
    }
    
    
balance = 100 

def admin_panel():
    user_perms = {0, 1}
    
    while True:
        print("\n\n||==================||")
        print("Панель с правами администратора")
        for key, value in Perms.rights.items():
            print(f"{key}. {value}")
        
        choice_admin = input("Выберите вариант: ")
        
        if not choice_admin.isdigit():
            print("Ошибка! Введите число.")
            continue
        
        choice_admin = int(choice_admin)
        
        if choice_admin not in Perms.rights:
            print("Ошибка! Такого варианта нет.")
            continue
        
        if choice_admin not in user_perms:
            print("У вас нет прав для выполнения этой команды!")
            continue
        
        if choice_admin == 0:
            print(f"Ваш баланс на данный момент: {balance}")
        elif choice_admin == 1:
            print("Выберите право, которое хотите получить:")
            for key, value in Perms.rights.items():
                if key not in user_perms:
                    print(f"{key}. {value}")
            
            perm_choice = input("Введите номер права: ")
            if not perm_choice.isdigit() or int(perm_choice) in user_perms or int(perm_choice) not in Perms.rights:
                print("Ошибка! Некорректный выбор.")
                continue
            
            user_perms.add(int(perm_choice))
            print(f"Вы получили право: {Perms.rights[int(perm_choice)]}")
        elif choice_admin == 2:
            print("Выберите право, которое хотите забрать:")
            for key in user_perms:
                if key > 1:
                    print(f"{key}. {Perms.rights[key]}")
            
            perm_choice = input("Введите номер права: ")
            if not perm_choice.isdigit() or int(perm_choice) not in user_perms or int(perm_choice) <= 1:
                print("Ошибка! Некорректный выбор.")
                continue
            
            user_perms.remove(int(perm_choice))
            print(f"Вы лишились права: {Perms.rights[int(perm_choice)]}")
        elif choice_admin == 3:
            print("Ваши права:")
            for key in user_perms:
                print(f"{key}. {Perms.rights[key]}")
        elif choice_admin == 4:
            print("Информация: Это панель администратора.")
        elif choice_admin == 5:
            print("Выход из панели...")
            break

admin_panel()    

def main():
        # login
    login = str(input("Введите логин: "))
    if login == "admin":
        print(f"Вы ввели логин: {login}")
    elif login == f"{login}":
        print(f"Вы ввели логин: {login}")
    else:
        print("Вы ввели что-то нето! попробуйте еще раз")        

    print(f"Логин: {login}")        
    password = getpass.getpass(str("Пароль: "))
    if password == "admin":
        print(f"Вы ввели пароль: {password}")
    elif password == "f{password}":
        print(f"Вы ввели пароль: {password}")    
            
    if login == "admin" and password == "admin":
        balance += 1000000
        is_loggin = True
        print("Добро пожаловать в систему!")
        print("Вы вошли в аккаунт Администратора!")
        print(f"Так как вы Администратор ваш баланс на данный момент - {balance}")
        admin_panel()
        
        
    elif login and password == f"{login} " and f"{password}":
        is_loggin = True
        print("Добро пожаловать в систему!")   
        print(f"Ваш баланс на данный момент - {balance}")
        # default panel coming soon
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()

    
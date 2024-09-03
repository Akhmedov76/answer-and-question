import threading

from decorator.decorator import log_decorator
# from role.super_admin.sup_admin import AdminManager
# from role.employees_for_admin.employees import Employees
from Auth.auth import Auth
from queries.queries import Table

auth = Auth


# employees = Employees()
# admin = AdminManager()


@log_decorator
def view_auth_menu() -> None:
    print("""
1. Login
2. Logout
    """)
    user_input: int = int(input("Choose menu: "))
    if user_input == 1:
        result_login = auth.login()
        if not result_login['is_login']:
            view_auth_menu()
        elif result_login['role'] == 'super_admin':
            pass
        elif result_login['role'] == 'manager':
            pass
        elif result_login['role'] == 'user':
            pass
    elif user_input == 2:
        print("Good bye!")
        if auth.logout():
            exit()
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_auth_menu()


@log_decorator
def view_admin_menu() -> None:
    print("""
1. Show statistics              # Tugalllanmagan
2. Logout
    """)
    choice: int = int(input("Enter your choice: "))
    if choice == 1:
        pass
    elif choice == 2:
        print("Good bye!")
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_admin_menu()


@log_decorator
def view_users_menu() -> None:
    print("""
1. Create a new test
2. Update test
3. Delete test
4. Show all tests
5. Logout
    """)
    choice: int = int(input("Enter your choice: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        print("Good bye!")
        view_admin_menu()
    else:
        print("Invalid choice!")
        view_users_menu()


@log_decorator
def view_choice_menu() -> None:
    print("""
1. Join test
2. Show all tests
3. My results
4. Logout
    """)
    choice: int = int(input("Enter your choice: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        print("Good bye!")
        view_choice_menu()
    else:
        print("Invalid choice!")
        view_choice_menu()


if __name__ == '__main__':
    # Run the authentication and table module
    auth = Auth()
    table = Table()
    threading.Thread(target=auth.logout).start()
    threading.Thread(target=table.create_all_table).start()
    view_auth_menu()

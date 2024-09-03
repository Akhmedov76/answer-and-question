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
            view_super_admin_menu()
            view_auth_menu()
        elif result_login['role'] == 'manager':
            view_manager_menu()
            view_auth_menu()
        elif result_login['role'] == 'user':
            view_employee_menu()
            view_auth_menu()
        view_auth_menu()
    elif user_input == 2:
        print("Good bye!")
        if auth.logout():
            exit()
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_auth_menu()


@log_decorator
def view_super_admin_menu() -> None:
    print("""
1. Manage departments 
2. Show statistics              # Tugalllanmagan
3. Logout
    """)
    choice: int = int(input("Enter your choice: "))
    if choice == 1:
        view_company_name()
        view_super_admin_menu()
    elif choice == 2:
        pass
    elif choice == 3:
        print("Good bye!")
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_super_admin_menu()


@log_decorator
def view_company_name() -> None:
    print("""
1. Add new company
2. Update company
3. Delete company
4. Show all company
5. Logout
    """)
    choice: int = int(input("Enter your choice: "))
    if choice == 1:
        if admin.add_department():
            view_company_name()
        else:
            view_company_name()
    elif choice == 2:
        admin.update_department()
        view_company_name()
    elif choice == 3:
        admin.delete_department()
        view_company_name()
    elif choice == 4:
        view_all_departments()
        view_company_name()
    elif choice == 5:
        print("Good bye!")
        view_super_admin_menu()
    else:
        print("Invalid choice!")
        view_company_name()


@log_decorator
def view_all_departments() -> None:
    print("""
1. View all company
2. View company by ID
3. Logout
    """)
    choice: int = int(input("Enter your choice: "))
    if choice == 1:
        admin.view_all_departments()
        view_all_departments()
    elif choice == 2:
        admin.view_department_by_id()
        view_all_departments()
    elif choice == 3:
        print("Good bye!")
        view_super_admin_menu()


@log_decorator
def view_manager_menu() -> None:
    print("""
1. Manage Employees
2. Show statistics              # Tugalllanmagan
3. Logout
    """)
    choice: int = int(input("Enter your choice: "))
    if choice == 1:
        view_main_menu()
        view_manager_menu()
    elif choice == 2:
        pass
    elif choice == 3:
        print("Good bye!")
        view_auth_menu()


@log_decorator
def view_main_menu() -> None:
    print("""
1. Add new employees
2. Update employees
3. Delete employees
4. Show all employees
5. Logout
    """)
    choice: int = int(input("Enter your choice: "))
    if choice == 1:
        employees.add_employees()
        view_main_menu()
    elif choice == 2:
        employees.update_employee()
        view_main_menu()
    elif choice == 3:
        employees.delete_employee()
        view_main_menu()
    elif choice == 4:
        employees.show_all_employees()
        view_main_menu()
    elif choice == 5:
        pass
    elif choice == 6:
        print("Good bye!")
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_main_menu()


@log_decorator
def view_employee_menu() -> None:
    print("""
1. Start work
2. End work
3. Show statistics                  # Tugalllanmagan
4. Show my data
5. Change password
6. Logout
    """)
    choice: int = int(input("Enter your choice: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        print("Good bye!")
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_employee_menu()


if __name__ == '__main__':
    # Run the authentication and table module
    auth = Auth()
    table = Table()
    threading.Thread(target=auth.logout).start()
    threading.Thread(target=table.create_all_table).start()
    view_auth_menu()

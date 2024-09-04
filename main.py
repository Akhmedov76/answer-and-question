import threading

from decorator.decorator import log_decorator
from queries.queries import show_all_statistics
from Auth.auth import Auth
from queries.queries import Table

auth = Auth
statistics = show_all_statistics()


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
        elif result_login['role'] == 'admin':
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
1. Show statistics
2. Logout
    """)
    choice: int = int(input("Enter your choice: "))
    if choice == 1:
        view_statistic_menu()
        view_admin_menu()
    elif choice == 2:
        print("Good bye!")
        view_auth_menu()
    else:
        print("Invalid choice!")
        view_admin_menu()


@log_decorator
def view_statistic_menu() -> None:
    print("""
1. Get total questions
2. Get average test score
3. Get worst test score
4. Get top 10 users
5. Get total attempts
6. Logout
    """)
    choice: int = int(input("Enter your choice: "))
    if choice == 1:
        if statistics.get_total_questions() > 0:
            print("Total questions:", statistics.get_total_questions())
            view_statistic_menu()
            threading.Timer(3.0, view_statistic_menu).start()
        else:
            print("No questions found!")
            view_statistic_menu()
            threading.Timer(3.0, view_statistic_menu).start()
    elif choice == 2:
        if statistics.get_average_score():
            print("Average test score:", statistics.get_average_score())
            view_statistic_menu()
            threading.Timer(3.0, view_statistic_menu).start()
        else:
            print("No test scores found!")
            view_statistic_menu()
            threading.Timer(3.0, view_statistic_menu).start()
    elif choice == 3:
        if statistics.get_worst_performers():
            print("Worst test score:", statistics.get_worst_performers())
            view_statistic_menu()
            threading.Timer(3.0, view_statistic_menu).start()
        else:
            print("No test scores found!")
            view_statistic_menu()
            threading.Timer(3.0, view_statistic_menu).start()
    elif choice == 4:
        if statistics.get_top_performers():
            print("Top 10 users:", statistics.get_top_performers())
            view_statistic_menu()
            threading.Timer(3.0, view_statistic_menu).start()
        else:
            print("No users found!")
            view_statistic_menu()
            threading.Timer(3.0, view_statistic_menu).start()
    elif choice == 5:
        if statistics.get_total_attempts() > 0:
            print("Total attempts:", statistics.get_total_attempts())
            view_statistic_menu()
            threading.Timer(3.0, view_statistic_menu).start()
        else:
            print("No attempts found!")
            view_statistic_menu()
            threading.Timer(3.0, view_statistic_menu).start()
    elif choice == 6:
        print("Good bye!")
        view_admin_menu()
    else:
        print("Invalid choice!")
        view_statistic_menu()


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

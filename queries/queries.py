from database_config.db_settings import Database, execute_query
from decorator.decorator import log_decorator


class Table:
    def __init__(self):
        self.db = Database()

    def create_users_table(self):
        """
        Create an employee table.
        """
        query = """
                            CREATE TABLE IF NOT EXISTS users (
                            id SERIAL PRIMARY KEY,
                            first_name VARCHAR(255) NOT NULL,
                            last_name VARCHAR(255) NOT NULL,
                            email VARCHAR(255) UNIQUE NOT NULL,
                            phone_number VARCHAR(20) NOT NULL,
                            username VARCHAR(50) UNIQUE NOT NULL,
                            password VARCHAR(255) NOT NULL,
                            status BOOLEAN DEFAULT FALSE NOT NULL,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            );
                        """
        with self.db as cursor:
            cursor.execute(query)
            return None

    def create_test_table(self):
        """
        Create a company table.
        """
        query = """
                    CREATE TABLE IF NOT EXISTS company (
                    id SERIAL PRIMARY KEY,
                    users BIGINT NOT NULL REFERENCES users(id),
                    name VARCHAR(255) NOT NULL,
                    status VARCHAR(255) NOT NULL DEFAULT False,
                    created_at TIMESTAMP DEFAULT DATE_TRUNC('minute', NOW())
                    );
                    """
        with self.db as cursor:
            cursor.execute(query)
            return None

    def create_question_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS question (
            id SERIAL PRIMARY KEY,
            test BIGINT NOT NULL REFERENCES test(id),
            name Varchar(255) NOT NULL,
            created_at TIMESTAMP DEFAULT DATE_TRUNC('minute', NOW())
        );
        """
        with self.db as cursor:
            cursor.execute(query)
            return None

    def create_option_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS option (
            id SERIAL PRIMARY KEY,
            question BIGINT NOT NULL REFERENCES question(id),
            name VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT DATE_TRUNC('minute', NOW())
        );
        """
        with self.db as cursor:
            cursor.execute(query)
            return None

    def create_all_table(self):
        self.create_users_table()
        self.create_test_table()
        self.create_question_table()
        self.create_option_table()


class QueryDepartment:
    def __init__(self):
        self.db = Database()

    @staticmethod
    @log_decorator
    def insert_department_table(name, address, phone_number, email, password):
        """
        Insert a new department into the company table.
        """
        query = """
        INSERT INTO company (name, address, phone_number, email,password)
        VALUES (%s, %s, %s, %s, %s)
        """
        params = (name, address, phone_number, email, password)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def update_department_table(id, name, address, phone_number, email, password):
        """
        Update a department in the company table.
        """
        query = "UPDATE company SET name=%s, address=%s, phone_number=%s, email=%s, password=%s WHERE id=%s"
        params = (name, address, phone_number, email, password, id)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def delete_department_table(id):
        """
        Delete a department from the company table.
        """
        query = "DELETE FROM company WHERE id=%s"
        params = (id,)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def view_departments_by_id(id):
        """
        Select a department from the company table by id.
        """
        query = "SELECT * FROM company WHERE id=%s"
        params = (id,)
        result = execute_query(query, params=params, fetch="one")
        return result

    @staticmethod
    @log_decorator
    def view_all_departments():
        """
        Select all departments from the company table.
        """
        query = "SELECT * FROM company"
        result = execute_query(query, fetch="all")
        return result


class QueryEmployees:
    @staticmethod
    @log_decorator
    def insert_employee_table(first_name, last_name, email, phone_number, username, password,
                              company_id, start_time='09:00:00', end_time='18:00:00'):
        """
        Insert a new employee into the employee table.
        """
        query = """
        INSERT INTO employee (first_name, last_name, email, phone_number, username, password, company, start_time, 
        end_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            first_name, last_name, email, phone_number, username, password, company_id, start_time, end_time)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def update_employee_table(employee_id, first_name, last_name, email, phone_number, username, password,
                              company_id):
        """
        Update an employee in the employee table.
        """
        query = """
        UPDATE employee SET first_name=%s, last_name=%s, email=%s, phone_number=%s, username=%s, password=%s, 
        company=%s WHERE id=%s
        """
        params = (
            first_name, last_name, email, phone_number, username, password, company_id, employee_id)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def delete_employee_table(employee_id):
        """
        Delete an employee from the employee table.
        """
        query = "DELETE FROM employee WHERE id=%s"
        execute_query(query, params=(employee_id,))
        return None

    @staticmethod
    @log_decorator
    def search_employee_by_email(email):
        """
        Retrieve employee data by email.
        """
        query = "SELECT * FROM employee WHERE email=%s"
        result = execute_query(query, fetch='one', params=(email,))
        return result

    @staticmethod
    @log_decorator
    def get_employee_by_phone_number(phone_number):
        """
        Retrieve employee data by phone number.
        """
        query = "SELECT * FROM employee WHERE phone_number=%s"
        result = execute_query(query, fetch='one', params=(phone_number,))
        return result

    # @staticmethod
    # @log_decorator
    # def get_employee_by_name(first_name, last_name):
    #     """
    #     Retrieve employee data by first name and last name.
    #     """
    #     query = "SELECT * FROM employee WHERE first_name=%s AND last_name=%s"
    #     result = execute_query(query, fetch='one', params=(first_name, last_name,))
    #     return result

    @staticmethod
    @log_decorator
    def change_employee_password(id, old_password, new_password):
        """
        Change employee password.
        """
        query = "UPDATE employee SET password_hash=%s WHERE id=%s AND password_hash=%s"
        params = (new_password, id, old_password)
        execute_query(query, params=params)
        return None


class QueryWorkSessions:
    def __init__(self):
        self.db = Database()

    @staticmethod
    @log_decorator
    def insert_work_session(employee_id, start_time):
        """
        Insert a new work session into the work_session table.
        """
        query = "INSERT INTO work_session (employee_id, start_time) VALUES (%s, %s)"
        params = (employee_id, start_time)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def update_work_session(session_id, end_time):
        """
        Update a work session in the work_session table.
        """
        query = "UPDATE work_session SET end_time=%s WHERE id=%s"
        params = (end_time, session_id)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def get_employee_work_sessions(employee_id):
        """
        Retrieve work sessions for a specific employee.
        """
        query = "SELECT * FROM work_session WHERE employee_id=%s ORDER BY start_time DESC"
        result = execute_query(query, fetch="all", params=(employee_id,))
        return result

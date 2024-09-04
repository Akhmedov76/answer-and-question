from database_config.db_settings import Database, execute_query
from decorator.decorator import log_decorator


class Table:
    def __init__(self):
        self.db = Database()

    @log_decorator
    def create_users_table(self):
        """
        Create users table.
        Created by Jasur use Ai!!!
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
                                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                );
                            """
        with self.db as cursor:
            cursor.execute(query)
            print("nnn")
            return None

    @log_decorator
    def create_test_table(self):
        """
        Create a test table.
        Craeted by Jasur use Ai!!!
        """
        query = """
                        CREATE TABLE IF NOT EXISTS test (
                        id SERIAL PRIMARY KEY,
                        users BIGINT NOT NULL REFERENCES users(id),
                        name VARCHAR(255) NOT NULL,
                        status BOOLEAN NOT NULL DEFAULT FALSE,
                        created_at TIMESTAMP DEFAULT DATE_TRUNC('minute', NOW())
                        );
                        """
        with self.db as cursor:
            cursor.execute(query)
            print("xato")
            return None

    @log_decorator
    def create_question_table(self):
        """
        Create a new question table
        Craeted by Jasur use Ai!!!
        """
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
            print("asaas")
            return None

    @log_decorator
    def create_option_table(self):
        """
        Create a new option table for question table
        Craeted by Jasur use Ai!!!
        """
        query = """
            CREATE TABLE IF NOT EXISTS quest_option (
                id SERIAL PRIMARY KEY,
                question BIGINT NOT NULL REFERENCES question(id),
                option_text VARCHAR(255) NOT NULL,
                correct BOOLEAN NOT NULL DEFAULT FALSE
            );
            """
        with self.db as cursor:
            cursor.execute(query)
            print("asdd")
            return None

    @log_decorator
    def create_attempt_table(self):
        """
        Create a new attempt table for user and question pairing
        Craeted by Jasur use Ai!!!
        """
        query = """
        CREATE TABLE IF NOT EXISTS attempt (
            id SERIAL PRIMARY KEY,
            user_id BIGINT NOT NULL REFERENCES users(id),
            question_id BIGINT NOT NULL REFERENCES question(id),
            created_at TIMESTAMP DEFAULT DATE_TRUNC('minute', NOW())
        );
        """
        with self.db as cursor:
            cursor.execute(query)
            print("Attempt")
            return None

    @log_decorator
    def create_answer_table(self):
        """
        Create a new answer table for user and question pairing and option selection
        Craeted by Jasur use Ai!!!
        """
        query = """
        CREATE TABLE IF NOT EXISTS answer (
            id SERIAL PRIMARY KEY,
            attempt BIGINT NOT NULL REFERENCES attempt(id),
            option_id BIGINT NOT NULL REFERENCES quest_option(id),
            created_at TIMESTAMP DEFAULT DATE_TRUNC('minute', NOW())
        );
        """
        with self.db as cursor:
            cursor.execute(query)
            print("Insert")
            return None

    @log_decorator
    def create_incorrect_answer_table(self):
        """
        Create a new incorrect answer table for user and question pairing and option selection
        Craeted by Jasur use Ai!!!
        """
        query = """
        CREATE TABLE IF NOT EXISTS incorrect_answer (
            id SERIAL PRIMARY KEY,
            attempt BIGINT NOT NULL REFERENCES attempt(id),
            option_id BIGINT NOT NULL REFERENCES quest_option(id),
            created_at TIMESTAMP DEFAULT DATE_TRUNC('minute', NOW())
        );
        """
        with self.db as cursor:
            cursor.execute(query)
            print("sdqwqse")
            return None

    @log_decorator
    def create_correct_answer_table(self):
        """
        Create a new correct answer table for user and question pairing
        Craeted by Jasur use Ai!!!
        """
        query = """
        CREATE TABLE IF NOT EXISTS correct_answer (
            id SERIAL PRIMARY KEY,
            question BIGINT NOT NULL REFERENCES question(id),
            created_at TIMESTAMP DEFAULT DATE_TRUNC('minute', NOW())
        );
        """
        with self.db as cursor:
            cursor.execute(query)
            print("adaqew")
            return None

    @log_decorator
    def create_score_table(self):
        """
        Create a new score table for user and test pairing
        Craeted by Jasur use Ai!!!
        """
        query = """
        CREATE TABLE IF NOT EXISTS score (
            id SERIAL PRIMARY KEY,
            user_id BIGINT NOT NULL REFERENCES users(id),
            test_id BIGINT NOT NULL REFERENCES test(id),
            created_at TIMESTAMP DEFAULT DATE_TRUNC('minute', NOW())
        );
        """
        with self.db as cursor:
            cursor.execute(query)
            print("wewre")
            return None

    @log_decorator
    def create_all_table(self):
        self.create_users_table()
        self.create_test_table()
        self.create_question_table()
        self.create_option_table()
        self.create_attempt_table()
        self.create_answer_table()
        self.create_incorrect_answer_table()
        self.create_correct_answer_table()
        self.create_score_table()


class QueryUsers:
    @staticmethod
    @log_decorator
    def insert_user_table(first_name, last_name, email, phone_number, username, password):
        """
        Insert a new user into the users table.
        """
        query = """
        INSERT INTO users (first_name, last_name, email, phone_number, username, password) VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (first_name, last_name, email, phone_number, username, password)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def update_user_table(user_id, first_name=None, last_name=None, email=None, phone_number=None,
                          username=None, password=None):
        """
        Update an existing user in the users table.
        """
        query = """
        UPDATE users SET """
        params = []
        if first_name:
            query += "first_name=%s,"
            params.append(first_name)
        if last_name:
            query += "last_name=%s,"
            params.append(last_name)
        if email:
            query += "email=%s,"
            params.append(email)
        if phone_number:
            query += "phone_number=%s,"
            params.append(phone_number)
        if username:
            query += "username=%s,"
            params.append(username)
        if password:
            query += "password=%s,"
            params.append(password)
        query = query[:-1] + " WHERE id=%s"
        params.append(user_id)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def delete_user_table(user_id):
        """
        Delete a user from the users table.
        """
        query = "DELETE FROM users WHERE id=%s"
        execute_query(query, params=(user_id,))
        return None

    @staticmethod
    @log_decorator
    def get_user_by_id(user_id):
        """
        Get a user from the users table by id.
        """
        query = "SELECT * FROM users WHERE id=%s"
        result = execute_query(query, fetch='one', params=(user_id,))
        return result

    @staticmethod
    @log_decorator
    def get_user_by_username(username):
        """
        Get a user from the users table by username.
        """
        query = "SELECT * FROM users WHERE username=%s"
        result = execute_query(query, fetch='one', params=(username,))
        return result

    @staticmethod
    @log_decorator
    def get_all_users():
        """
        Get all users from the users table.
        """
        query = "SELECT * FROM users"
        result = execute_query(query, fetch='all')
        return result

    @staticmethod
    @log_decorator
    def authenticate_user(username, password):
        """
        Authenticate a user by username and password.
        """
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        result = execute_query(query, fetch='one', params=(username, password,))
        return result


class QueryTests:
    @staticmethod
    @log_decorator
    def insert_test_table(user_id, name, status=False):
        """
        Insert a new test into the test table.
        """
        query = """
            INSERT INTO test (users, name, status) VALUES (%s, %s, %s)
            """
        params = (user_id, name, status)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def update_test_table(test_id, name=None, status=None):
        """
        Update an existing test in the test table.
        """
        query = """
        UPDATE test SET """
        params = []
        if name:
            query += "name=%s,"
            params.append(name)
        if status:
            query += "status=%s,"
            params.append(status)
        query = query[:-1] + " WHERE id=%s"
        params.append(test_id)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def delete_test_table(test_id):
        """
        Delete a test from the test table.
        """
        query = "DELETE FROM test WHERE id=%s"
        execute_query(query, params=(test_id,))
        return None

    @staticmethod
    @log_decorator
    def get_test_by_id(test_id):
        """
        Get a test from the test table by id.
        """
        query = "SELECT * FROM test WHERE id=%s"
        result = execute_query(query, fetch='one', params=(test_id,))
        return result

    @staticmethod
    @log_decorator
    def get_all_tests_by_user_id(user_id):
        """
        Get all tests from the test table by user id.
        """
        query = "SELECT * FROM test WHERE user_id=%s"
        result = execute_query(query, fetch='all', params=(user_id,))
        return result

    @staticmethod
    @log_decorator
    def get_active_test_by_user_id(user_id):
        """
        Get the active test from the test table by user id.
        """
        query = "SELECT * FROM test WHERE user_id=%s AND status=True"
        result = execute_query(query, fetch='one', params=(user_id,))
        return result


class QueryQuestions:
    @staticmethod
    @log_decorator
    def insert_question_table(test_id, question):
        """
        Insert a new question into the question table.
        """
        query = """
        INSERT INTO question (test_id, question) VALUES (%s, %s)
        """
        params = (test_id, question)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def update_question_table(question_id, question=None):
        """
        Update an existing question in the question table.
        """
        query = """
        UPDATE question SET """
        params = []
        if question:
            query += "question=%s,"
            params.append(question)
        query = query[:-1] + " WHERE id=%s"
        params.append(question_id)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def delete_question_table(question_id):
        """
        Delete a question from the question table.
        """
        query = "DELETE FROM question WHERE id=%s"
        execute_query(query, params=(question_id,))
        return None

    @staticmethod
    @log_decorator
    def get_question_by_id(question_id):
        """
        Get a question from the question table by id.
        """
        query = "SELECT * FROM question WHERE id=%s"
        result = execute_query(query, fetch='one', params=(question_id,))
        return result

    @staticmethod
    @log_decorator
    def get_all_questions_by_test_id(test_id):
        """
        Get all questions from the question table by test id.
        """
        query = "SELECT * FROM question WHERE test_id=%s"
        result = execute_query(query, fetch='all', params=(test_id,))
        return result


class QueryOptions:
    @staticmethod
    @log_decorator
    def insert_option_table(question_id, option):
        """
        Insert a new option into the option table.
        """
        query = """
                INSERT INTO quest_option (question_id, option_text) VALUES (%s, %s)
                """
        params = (question_id, option)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def update_option_table(option_id, option=None):
        """
        Update an existing option in the option table.
        """
        query = """
        UPDATE option SET """
        params = []
        if option:
            query += "option=%s,"
            params.append(option)
        query = query[:-1] + " WHERE id=%s"
        params.append(option_id)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def delete_option_table(option_id):
        """
        Delete an option from the option table.
        """
        query = "DELETE FROM option WHERE id=%s"
        execute_query(query, params=(option_id,))
        return None

    @staticmethod
    @log_decorator
    def get_option_by_id(option_id):
        """
        Get an option from the option table by id.
        """
        query = "SELECT * FROM option WHERE id=%s"
        result = execute_query(query, fetch='one', params=(option_id,))
        return result

    @staticmethod
    @log_decorator
    def get_all_options_by_question_id(question_id):
        """
        Get all options from the option table by question id.
        """
        query = "SELECT * FROM option WHERE question_id=%s"
        result = execute_query(query, fetch='all', params=(question_id,))
        return result

    @staticmethod
    @log_decorator
    def get_correct_options_by_question_id(question_id):
        """
        Get all correct options from the option table by question id.
        """
        query = "SELECT * FROM option WHERE question_id=%s AND is_correct=True"
        result = execute_query(query, fetch='all', params=(question_id,))
        return result

    @staticmethod
    @log_decorator
    def get_incorrect_options_by_question_id(question_id):
        """
        Get all incorrect options from the option table by question id.
        """
        query = "SELECT * FROM option WHERE question_id=%s AND is_correct=False"
        result = execute_query(query, fetch='all', params=(question_id,))
        return result


class QueryAttempts:
    @staticmethod
    @log_decorator
    def insert_attempt_table(user_id, test_id):
        """
        Insert a new attempt into the attempt table.
        """
        query = """
        INSERT INTO attempt (user_id, test_id) VALUES (%s, %s)
        """
        params = (user_id, test_id)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def update_attempt_table(attempt_id, score=None):
        """
        Update an existing attempt in the attempt table.
        """
        query = """
        UPDATE attempt SET """
        params = []
        if score:
            query += "score=%s,"
            params.append(score)
        query = query[:-1] + " WHERE id=%s"
        params.append(attempt_id)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def delete_attempt_table(attempt_id):
        """
        Delete an attempt from the attempt table.
        """
        query = "DELETE FROM attempt WHERE id=%s"
        execute_query(query, params=(attempt_id,))
        return None

    @staticmethod
    @log_decorator
    def get_attempt_by_id(attempt_id):
        """
        Get an attempt from the attempt table by id.
        """
        query = "SELECT * FROM attempt WHERE id=%s"
        result = execute_query(query, fetch='one', params=(attempt_id,))
        return result

    @staticmethod
    @log_decorator
    def get_all_attempts_by_user_id(user_id):
        """
        Get all attempts from the attempt table by user id.
        """
        query = "SELECT * FROM attempt WHERE user_id=%s"
        result = execute_query(query, fetch='all', params=(user_id,))
        return result


class QueryAnswerAttempts:
    @staticmethod
    @log_decorator
    def insert_answer_attempt_table(attempt_id, question_id, option_id):
        """
        Insert a new answer attempt into the answer_attempt table.
        """
        query = """
        INSERT INTO answer_attempt (attempt_id, question_id, option_id) VALUES (%s, %s, %s)
        """
        params = (attempt_id, question_id, option_id)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def update_answer_attempt_table(answer_attempt_id, is_correct=None):
        """
        Update an existing answer attempt in the answer_attempt table.
        """
        query = """
        UPDATE answer_attempt SET """
        params = []
        if is_correct:
            query += "is_correct=%s,"
            params.append(is_correct)
        query = query[:-1] + " WHERE id=%s"
        params.append(answer_attempt_id)
        execute_query(query, params=params)
        return None

    @staticmethod
    @log_decorator
    def delete_answer_attempt_table(answer_attempt_id):
        """
        Delete an answer attempt from the answer_attempt table.
        """
        query = "DELETE FROM answer_attempt WHERE id=%s"
        execute_query(query, params=(answer_attempt_id,))
        return None

    @staticmethod
    @log_decorator
    def get_answer_attempt_by_id(answer_attempt_id):
        """
        Get an answer attempt from the answer_attempt table by id.
        """
        query = "SELECT * FROM answer_attempt WHERE id=%s"
        result = execute_query(query, fetch='one', params=(answer_attempt_id,))
        return result

    @staticmethod
    @log_decorator
    def get_all_answer_attempts_by_attempt_id(attempt_id):
        """
        Get all answer attempts from the answer_attempt table by attempt id.
        """
        query = "SELECT * FROM answer_attempt WHERE attempt_id=%s"
        result = execute_query(query, fetch='all', params=(attempt_id,))
        return result


class QueryScoring:
    @staticmethod
    @log_decorator
    def calculate_score(attempt_id):
        """
        Calculate the score for an attempt.
        """
        correct_options = QueryAnswerAttempts.get_all_answer_attempts_by_attempt_id(attempt_id)
        total_questions = len(QueryAnswerAttempts.get_all_answer_attempts_by_attempt_id(attempt_id))
        score = sum(answer_attempt['is_correct'] for answer_attempt in correct_options) / total_questions
        QueryAttempts.update_attempt_table(attempt_id, score=score)
        return score

    @staticmethod
    @log_decorator
    def calculate_percentage(attempt_id):
        """
        Calculate the percentage for an attempt.
        """
        score = QueryScoring.calculate_score(attempt_id)
        percentage = (score / 1) * 100
        return percentage


class show_all_statistics:
    @staticmethod
    @log_decorator
    def get_total_questions():
        """
        Get the total number of questions in the question table.
        """
        query = "SELECT COUNT(*) FROM question"
        result = execute_query(query, fetch='one')
        return result['count']

    @staticmethod
    @log_decorator
    def get_total_options():
        """
        Get the total number of options in the option table.
        """
        query = "SELECT COUNT(*) FROM option"
        result = execute_query(query, fetch='one')
        return result['count']

    @staticmethod
    @log_decorator
    def get_total_attempts():
        """
        Get the total number of attempts in the attempt table.
        """
        query = "SELECT COUNT(*) FROM attempt"
        result = execute_query(query, fetch='one')
        return result['count']

    @staticmethod
    @log_decorator
    def get_average_score():
        """
        Get the average score of all attempts.
        """
        attempts = QueryAttempts.get_all_attempts_by_user_id(None)
        total_score = sum(attempt['score'] for attempt in attempts)
        average_score = total_score / len(attempts) if attempts else 0
        return average_score

    @staticmethod
    @log_decorator
    def get_top_performers():
        """
        Get the top 10 users with the highest average score.
        """
        query = """
        SELECT user.id, user.username, AVG(attempt.score) as average_score
        FROM user
        JOIN attempt ON user.id = attempt.user_id
        GROUP BY user.id, user.username
        ORDER BY average_score DESC
        LIMIT 10
        """
        result = execute_query(query, fetch='all')
        return result

    @staticmethod
    @log_decorator
    def get_worst_performers():
        """
        Get the top 10 users with the lowest average score.
        """
        query = """
        SELECT user.id, user.username, AVG(attempt.score) as average_score
        FROM user
        JOIN attempt ON user.id = attempt.user_id
        GROUP BY user.id, user.username
        ORDER BY average_score ASC
        LIMIT 10
        """
        result = execute_query(query, fetch='all')
        return result

    @staticmethod
    @log_decorator
    def get_most_correct_answers():
        """
        Get the top 10 users who answered the most questions correctly.
        """
        query = """
        SELECT user.id, user.username, COUNT(answer_attempt.is_correct) as correct_answers
        FROM user
        JOIN attempt ON user.id = attempt.user_id
        JOIN answer_attempt ON attempt.id = answer_attempt.attempt_id
        WHERE answer_attempt.is_correct = True
        GROUP BY user.id, user.username
        ORDER BY correct_answers DESC
        LIMIT 10
        """
        result = execute_query(query, fetch='all')
        return result

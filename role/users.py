"""
1. Create a new test
2. Update test
3. Delete test
4. Show all tests
    """
from database_config.db_settings import Database, execute_query


class UserManager:
    def __init__(self):
        self.db = Database()

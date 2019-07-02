import contextlib
import os
import subprocess
from datetime import datetime, timedelta


def test_database_setup():
    """
    Prepares a new sqlite database using the schema from the main database but none of the data.
    Then, inserts test data into it via Django.
    """

    TEST_DB_NAME = 'test_db.sqlite3'
    with contextlib.suppress(FileNotFoundError):
        TIMEOUT_SECONDS = 60
        cutoff_time = datetime.now() + timedelta(seconds=TIMEOUT_SECONDS)
        db_deleted = False
        while not db_deleted and datetime.now() < cutoff_time:
            try:
                os.remove(TEST_DB_NAME)
                db_deleted = True
            except PermissionError:
                # DB file lock is probably still held by last Django server instance.
                # Let's give it a moment to release it.
                pass

        if not db_deleted:
            raise TimeoutError(f"Could not delete {TEST_DB_NAME}")

    # Just doing:
    # `subprocess.call(f'sqlite3 db.sqlite3 .schema | sqlite3 {self.TEST_DB_NAME}', shell=True)`
    # would be nicer, but unfortunately sqlite creates a default table (sqlite_sequence) that we need to
    # remove from the schema before passing it back in again
    schema_byte_string = subprocess.check_output('sqlite3 db.sqlite3 .schema', shell=True)
    schema_string = str(schema_byte_string, 'utf-8')
    schema_one_line = schema_string.replace('\r','').replace('\n','')
    schema_without_sqlite_sequence = schema_one_line.replace('CREATE TABLE sqlite_sequence(name,seq);','')
    subprocess.call(f'echo {schema_without_sqlite_sequence} | sqlite3 {TEST_DB_NAME}', shell=True)

    # populate new database as is needed for testing
    with open('logs/test_setup_log.txt', 'a') as log:
        subprocess.call(
            ['py', 'manage.py', 'test_setup', '--settings=charity_configuration.test_settings'],
            stdout=log,
        )


if __name__ == '__main__':
    test_database_setup()

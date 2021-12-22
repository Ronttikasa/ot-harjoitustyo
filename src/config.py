import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

GOALS_FILENAME = os.getenv('GOALS_FILENAME') or 'training_goals.txt'
GOALS_FILE_PATH = os.path.join(dirname, '..',  'data', GOALS_FILENAME)

JOURNAL_FILENAME = os.getenv('JOURNAL_FILENAME') or 'trainingjournal.txt'
JOURNAL_FILE_PATH = os.path.join(dirname,  '..', 'data', JOURNAL_FILENAME)

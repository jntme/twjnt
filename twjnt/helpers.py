"""Contains the helper functions for twjnt"""
import pickle, os

PICKLE_FILE_NAME = "data.pickle"


def save_access_tokens(access_token, access_token_secret):
    """
    Pickles the access_token and the access_token_secret for reuse.
    """

    if not os.path.exists("data.pickle"):

        file = open(PICKLE_FILE_NAME, 'xb')

    else:
        file = open('data.pickle', 'wb')

    pickle.dump((access_token, access_token_secret), file, pickle.HIGHEST_PROTOCOL)


def load_access_tokens() -> (str, str):
    """
    Returns the pickled access_token and access_token_secret if existing.

    """

    if os.path.exists("data.pickle"):

        file = open(PICKLE_FILE_NAME, 'rb')

        return pickle.load(file)
    else:
        return False



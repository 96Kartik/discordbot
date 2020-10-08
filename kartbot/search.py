import os, requests

from db_utils import db

# to load .env file on shell env omm server
from dotenv import load_dotenv

load_dotenv()


def store_search_history(search_text, author):
    """Method to store Search Queries on the Database"""
	db.history.insert_one({'text':search_text, "user":author.name})


def get_search_history_by_keywords(search_text, author):
    """Method to fetch Search Queries on the Database"""
    word_search = search_text.strip().split(' ')
    keyword_history_list = list()
    for word in word_search:
        history=list(db.history.find({'text':{'$regex': ".*"+word+".*", '$options': 'i'}, "user":author.name}))
        if history:
            for hist in history:
                if hist.get('text') not in keyword_history_list :
                    keyword_history_list.append('`{}`'.format(hist.get('text')))
    if not keyword_history_list:
        return []
    return keyword_history_list


def search_on_google(search_text):
    """Method to Seacrh Web using Google Custom Search JSON API"""
    result = requests.get("https://www.googleapis.com/customsearch/v1?key={}&q={}&cx={}".format(os.getenv('G_API_KEY'), search_text, os.getenv('SE_ID')))
    if result.status_code == 200:
        search_results = result.json().get('items')
        if len(search_results) < 1:
            return []
        else:
            return search_results
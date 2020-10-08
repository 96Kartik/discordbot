import os
import pymongo

# to load .env file on shell env omm server
from dotenv import load_dotenv

load_dotenv()

# Cloud MongoDB connection variables
user_name = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database_name = os.getenv('DB_NAME')
cluster_name = os.getenv('CLUSTER_NAME')

# Cloud MongoDB raw connection URI
cluster_url="mongodb+srv://{}:{}@{}.gcp.mongodb.net/?retryWrites=true&w=majority".format(user_name,password,cluster_name)

# Cloud MongoDB client
db_client = pymongo.MongoClient(cluster_url)

db = db_client[database_name]
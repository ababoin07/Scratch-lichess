import scratchattach as sa
import time
import random
import json
def save_database(database, filename):
    with open(filename, "w") as file:
        json.dump(database, file)
        print(f"Database saved on {filename}.")
def load_database(filename):
    try:
        with open(filename, "r") as file:
            database = json.load(file)
            print(f"Database opened from {filename}")
            return database
    except FileNotFoundError:
        print(f"File {filename} not found")
        return {}
database = load_database("database.json")
session = sa.login_by_id("SESSION UID")
cloud = session.connect_cloud("1103966178")
client = cloud.requests()
@client.request
def create(user,password):
    global database
    if user in database:
        return 0
    database[user] = {"password":password}
    return 1
@client.request
def login(user,password):
    global database
    if user in database:
        if database[user]["password"] == password:
            return 1
    return 0
@client.event
def on_ready():
    print("Request handler is running")
client.start(thread=True)
#client.send("hey")
while True:
    time.sleep(2)
    save_database(database,"database.json")

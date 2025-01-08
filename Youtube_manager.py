# PYTHON PROJECT

from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("localhost",27017)
db = client["ytManager"]
collection = db["videos"]

# print(collection)

def list_videos():
    for video in collection.find():
        print(f"ID: {video["_id"]} TITLE: {video["name"]} DURATION : {video["time"]}")

def add_video(name,time):
    collection.insert_one({"name" : name, "time" : time})

def update_video(id,new_name,new_time):
    collection.update_one({"_id" : ObjectId(id)},{"$set" : {"name" : new_name, "time" : new_time}})

def delete_video(id):
    collection.delete_one({"_id" : ObjectId(id)})

def main():

    while True:
        print("\n****************************** YOUTUBE MANAGER APP ******************************")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit App")
        print("\n*********************************************************************************")

        choice = input("Enter your choice : ")

        match choice:
            case '1': 
                list_videos()
            case '2':
                name = input("Enter the title of video : ")
                time = input("Enter the duration of video : ")
                add_video(name,time)
            case '3':
                id = input("Enter the id of video to update : ")
                new_name = input("Enter the new title : ")
                new_duration = input("Enter the new duration : ")
                update_video(id,new_name,new_duration)
            case '4':
                id = input("Enter the id of video to delete : ")
                delete_video(id)
            case '5':
                break
            case _:
                print("Invalid Choice !!")


if __name__ == "__main__":
    main()
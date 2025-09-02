from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['school_activities']
activities_collection = db['activities']

# Initial activities data
activities = {
    "Chess Club": {
        "_id": "Chess Club",
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "_id": "Programming Class",
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "_id": "Gym Class",
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "_id": "Soccer Team",
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["lucas@mergington.edu", "mia@mergington.edu"]
    },
    "Basketball Club": {
        "_id": "Basketball Club",
        "description": "Practice basketball skills and play friendly games",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["liam@mergington.edu", "ava@mergington.edu"]
    },
    "Art Workshop": {
        "_id": "Art Workshop",
        "description": "Explore painting, drawing, and sculpture techniques",
        "schedule": "Mondays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["ella@mergington.edu", "noah@mergington.edu"]
    },
    "Drama Club": {
        "_id": "Drama Club",
        "description": "Act, direct, and produce school plays and performances",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["jack@mergington.edu", "grace@mergington.edu"]
    },
    "Math Olympiad": {
        "_id": "Math Olympiad",
        "description": "Prepare for math competitions and solve challenging problems",
        "schedule": "Fridays, 2:00 PM - 3:30 PM",
        "max_participants": 10,
        "participants": ["henry@mergington.edu", "chloe@mergington.edu"]
    },
    "Science Club": {
        "_id": "Science Club",
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["ben@mergington.edu", "zoe@mergington.edu"]
    }
}

# Insert activities into MongoDB
activities_collection.insert_many(list(activities.values()))
print("Activities imported successfully!")

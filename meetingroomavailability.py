import datetime
from meetingroom import MeetingRoom
from helpers import get_time_hour_from_String

if __name__ == "__main__":
    inputdate = input("When is your meeting? (yyyy-mm-dd) ")
    duration = input("What is your meeting duration in minutes? ")
    time = input("Input your time in 24 hour format ex: 15:30 (or) 14:15: ")

    split_time = get_time_hour_from_String(time)
    hour = split_time["hour"]
    minute = split_time["minute"]

    if inputdate == "":
        date = datetime.datetime.now()
    else:
        date = datetime.datetime.strptime(inputdate, "%Y-%m-%d")

    # Load the available meeting rooms
    # Read the list of meeting rooms from the txt file in the solution path
    text_file = open("roomslist.txt", "r")
    rooms = text_file.readlines()

    #Foreach room available in the list loop through the availability function
    for room in rooms:
        meetingRoomObj = MeetingRoom(
            date.replace(hour=hour, minute=minute).strftime("%Y-%m-%d %H:%M:%S"),
            duration,
            room,
        )
        meetingRoomObj.checkRoomAvailability()
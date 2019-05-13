# THis is a method to split the time stamp provied by the user in the UI to hour and minute


def get_time_hour_from_String(time):

    if time == "":
        hour = int(datetime.datetime.now().hour)
        minute = int(datetime.datetime.now().minute)
    else:
        hour = int(time.split(":")[0])
        if len(time.split(":")) > 1:
            minute = int(time.split(":")[1])
        else:
            minute = 00
    return {"hour": hour, "minute": minute}


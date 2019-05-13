# Class to hold the meeting room details and to check for the availabiltiy
import win32com.client
import pywintypes
import datetime

class MeetingRoom:
    def __init__(self, inputDate, duration, locationMail):
        self.inputDate = inputDate
        self.oOutlook = win32com.client.Dispatch("Outlook.Application")
        self.bookings = self.oOutlook.CreateItem(1)
        self.bookings.Start = inputDate
        self.bookings.Duration = duration
        self.bookings.Subject = "Meeting"
        self.bookings.MeetingStatus = 1
        self.roomRecipient = self.bookings.Recipients.Add(locationMail)
        self.splitMinutes = int(duration)

    def checkRoomAvailability(self):
        bookingDateTime = datetime.datetime.strptime(
            self.inputDate, "%Y-%m-%d %H:%M:%S"
        )
        self.roomRecipient.resolve

        availabilityInfo = self.roomRecipient.FreeBusy(
            bookingDateTime, self.splitMinutes, True
        )

        dt = bookingDateTime
        newTime = dt.replace(hour=0, minute=0, second=0, microsecond=0)

        for isAvailable in availabilityInfo:
            if newTime >= bookingDateTime:
                if isAvailable == "0":
                    print("Room available in", self.roomRecipient)
                    break
                elif isAvailable != "0":
                    print("Room NOT available in", self.roomRecipient)
                    break
                    
            newTime = newTime + datetime.timedelta(minutes=self.splitMinutes)

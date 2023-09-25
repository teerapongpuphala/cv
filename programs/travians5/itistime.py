import datetime


class Itisthetime:
    def __init__(self,DateTmeDestinationString,TimeSpanString):
        self.DateTmeDestinationString = DateTmeDestinationString
        self.TimeSpanString = TimeSpanString
        self.timeDelay = 3.45

    def spend_time(self):
        timeSpendList = self.TimeSpanString.split(":")
        timeSpendHour = int(timeSpendList[0])*3600
        timeSpendMin = int(timeSpendList[1])*60
        timeSpendSec = int(timeSpendList[2])
        sumTimeSpend = timeSpendMin+timeSpendSec+timeSpendHour
        return sumTimeSpend

    def departure_time(self):
        timeInputList = self.DateTmeDestinationString.split("-")
        timeInputYe = int(timeInputList[0])
        timeInputMo = int(timeInputList[1])
        timeInputDa = int(timeInputList[2])
        timeInputHour = int(timeInputList[3])
        timeInputMin = int(timeInputList[4])
        timeInputSec = int(timeInputList[5])
        arrTime = datetime.datetime(timeInputYe,timeInputMo,timeInputDa,timeInputHour,timeInputMin,timeInputSec)
        depart = arrTime - datetime.timedelta(0,self.spend_time()+self.timeDelay)
        return depart

    def send_time(self):
        while(True):
            now = datetime.datetime.now()
            departureTime = self.departure_time()
            if now.day == departureTime.day and now.hour == departureTime.hour and now.minute == departureTime.minute and now.second == (departureTime.second):
                print("Send at: "+str(datetime.datetime.now()))
                return True


# TimeSpanString = "00:01:00"
# DateTmeDestinationString = "2020-07-17-22-44-10"

# myTime = Itisthetime(DateTmeDestinationString,TimeSpanString)
# # ---------------------------------------------------------------------------------------------------
# if(myTime.send_time()):
#     print("done")







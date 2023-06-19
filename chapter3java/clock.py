class Clock:

    def __init__(self, hour: int, minute: int, seconds: int):
        self.hour = hour
        self.minute = minute
        self.seconds = seconds

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        if 0 <= hour <= 23:
            self.__hour = hour
        else:
            raise ValueError("hour is not below  ")

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute):
        if 0 <= minute <= 59:
            self.__minute = minute
        else:
            raise ValueError("balance cannot be negative")

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds):
        if 0 <= seconds <= 59:
            self.__seconds = seconds
        else:
            raise ValueError("balance cannot be negative")

    def __str__(self):
        return f"time {self.hour} {self.minute} {self.seconds}"

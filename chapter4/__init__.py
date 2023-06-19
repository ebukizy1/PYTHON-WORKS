class television:
    isOn = False
    volume = 0
    channel = 0

    @classmethod
    def toggleOn(cls):
        cls.isOn = not cls.isOn

    @classmethod
    def decrease_volume(cls):
        if 0 < cls.volume <= 100:
            cls.volume -= 1

    @classmethod
    def increase_volume(cls):
        if cls.volume < 100:
            cls.volume += 1

    @classmethod
    def increase_channel(cls):
        if cls.volume < 100:
            cls.volume -= 1

    @classmethod
    def decrease_volume(cls):
        if cls.volume < 100:
            cls.volume -= 1


television1 = television
# television1.toggleOn()
television1.decrease_volume()
print(television1.volume)

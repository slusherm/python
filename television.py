class Television:
    """
    Class for the functions of a basic TV
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method that sets the default TV setting
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method that sets the TV either on or off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Method that mutes or unmutes the TV
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        Method that sets the channel one higher
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method that sets the channel one lower
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1


    def volume_up(self) -> None:
        """
        Method that turns the volume up by 1
        """
        if self.__status:
            if self.__volume != Television.MAX_VOLUME:
                self.__volume += 1
                self.__muted = False

    def volume_down(self) -> None:
        """
        Method that turns the volume down by 1
        """
        if self.__status:
            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1
                self.__muted = False

    def __str__(self) -> str:
        """
        Method that prints the current TV settings
        :return: TV's current settings for power, channel, and volume
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
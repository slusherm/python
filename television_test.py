import pytest
from television import *

class Test:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_innit(self):
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'  #default values

    def test_power(self):
        self.tv.power()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'  #when tv is on
        self.tv.power()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'  #when tv is off

    def test_mute(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'  #when tv is on, volume increased once,
        #and tv muted

        self.tv.mute()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'  #when tv is on and unmuted

        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 1'  #when tv is off and muted

        self.tv.mute()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 1'  #when tv is on and muted

    def test_channel_up(self):
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0' #tv is off and channel increased

        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 1, Volume = 0'  #tv is on and channel increased

        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'  #tv is on and channel is increased
        #past maximum channel

    def test_channel_down(self):
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0' #tv is off and channel decreased

        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = True, Channel = 3, Volume = 0'  #tv is on and channel decreased
        #past minimum channel

    def test_volume_up(self):
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'  #tv is off and volume increased

        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'  # tv is on and volume increased

        self.tv.mute()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 2'  # tv is on, muted, and volume increased

        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 2'  # tv is on and volume increased
        #past maximum volume

    def test_volume_down(self):
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'  #tv is off and volume decreased

        self.tv.power()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'  #tv is on and volume decreased
        #past minimum volume

        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1' #tv is on and volume decreased from
        #maximum volume

        self.tv.mute()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0' #tv is on, muted, and volume decreased
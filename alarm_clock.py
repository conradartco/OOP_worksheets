class AlarmClock:
    def __init__(self):
        self.current_time = '10:00'
        self.alarm_on = False
        self.alarm_set_time = ''
    
    def time_change(self):
        print("The time is currently ", self.current_time)
        self.current_time = input("What time is it? : ")
        print("The time is currently ", self.current_time)

    def alarm_toggle(self):
        self.alarm_input = input("Set alarm status: ON or OFF : ")
        if self.alarm_input == "ON":
            self.alarm_on is True
            print("The alarm is currently: ON")
        elif self.alarm_input == "OFF":
            self.alarm_on is False
            print("The alarm is currently: OFF")

    def alarm_set(self):
        self.alarm_set_time = input("What time would you like to set the alarm? : ")
        print("The current alarm time is set for: ", self.alarm_set_time)
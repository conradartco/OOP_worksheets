class CellPhone:
    def __init__(self,model):
        self.model = model
        self.number = '555-666-0420'
        self.contacts = {
            "Mom": "354-985-4002",
            "God": "888-HEAVENS",
            "Elmo": "123-456-7890"
        }
        self.messages = []
        self.vibrate = False

    def text_mesg(self, message):
        print(message)
        self.messages.append(message)

    def vib_mode(self, vibe_check):
        if vibe_check == 'ON':
            self.vibrate is True
            print("Vibration is ON")
        elif vibe_check == 'OFF':
            self.vibrate is False
            print("Vibration is OFF")

    def send_mesg(self):
        self.message_str = input("Begin a new text message: ")
        print(self.message_str)


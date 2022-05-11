from cell_phone import CellPhone

cell_one = CellPhone('Motorolla')
print(cell_one.contacts)

message_one = "Hello! We've been trying to reach you about your cars' extended warranty..."
message_two = "Okay but, WHERE in the WORLD is Carmen SanDiego?? She's been missing for YEARS!!"
cell_one.text_mesg(message_one)
cell_one.text_mesg(message_two)

print(cell_one.messages)

cell_one.send_mesg()
cell_one.vib_mode("ON")

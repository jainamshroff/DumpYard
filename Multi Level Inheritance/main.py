class ElectronicDevice():
    battery = 1
    weight = 100

class PocketGadget(ElectronicDevice):
    battery = 6

class MobilePhone(PocketGadget):
    weight = 20

electronicdevice = ElectronicDevice()
pocketgadget = PocketGadget()
mobilephone = MobilePhone()

print(electronicdevice.battery)
print(pocketgadget.battery)
print(mobilephone.battery)

print(electronicdevice.weight)
print(pocketgadget.weight)
print(mobilephone.weight)


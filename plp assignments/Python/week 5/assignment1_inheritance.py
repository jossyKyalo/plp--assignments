# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.battery += amount
        print(f"Battery charged to {self.battery}%")

    def __str__(self):
        return f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}%"

# Child class (inheritance)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        super().__init__(brand, model, storage, battery)
        self.gpu = gpu

    #  polymorphism  
    def call(self, number):
        print(f"{self.brand} {self.model} uses gaming headset to call {number}")

    def play_game(self, game):
        if self.battery > 20:
            print(f"Playing {game} on {self.gpu} GPU")
        else:
            print("Battery too low to play!")

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 75)
phone2 = GamingSmartphone("Asus", "ROG Phone 6", 512, 50, "Adreno 730")

print(phone1)
phone1.call("123-456-789")
phone1.charge(10)

print("\n" + str(phone2))
phone2.call("987-654-321")
phone2.play_game("PUBG Mobile")
 
# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self._storage = storage          # Protected attribute (single underscore)
        self.__battery = battery         # Private attribute (double underscore)
        self.is_on = False

    # Method to turn on the phone
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    # Method to turn off the phone
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    # Method to install an app
    def install_app(self, app_name):
        if self.is_on:
            print(f"Installing {app_name} on {self.brand} {self.model}...")
        else:
            print(f"Cannot install {app_name}. Please turn on the phone first.")

    # Method to show specifications
    def show_specs(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self._storage}GB, Battery: {self.__battery}mAh")

# Create an object of Smartphone
phone = Smartphone("Samsung", "Galaxy S21", 128, 4000)
phone.show_specs()
phone.turn_on()
phone.install_app("WhatsApp")
phone.turn_off()

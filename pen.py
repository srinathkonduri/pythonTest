class Pen:
    def __init__(self, brand, color, ink_type):
        # Initialize the Pen's attributes
        self.brand = brand
        self.color = color
        self.ink_type = ink_type
        self.is_inked = True  # Assume the pen has ink by default

    def write(self, text):
        # Simulate writing with the pen
        if self.is_inked:
            print(f"{self.brand} {self.color} pen writes: {text}")
        else:
            print(f"The pen is out of ink. Please refill the ink.")

    def refill(self):
        # Refills the pen with ink
        self.is_inked = True
        print(f"The {self.brand} pen has been refilled with {self.ink_type} ink.")

    def get_info(self):
        # Display pen information
        return f"Pen brand: {self.brand}, Color: {self.color}, Ink type: {self.ink_type}"

# Creating a Pen object
pen1 = Pen(brand="Parker", color="blue", ink_type="ballpoint")

# Writing with the pen
pen1.write("Hello, World!")

# Displaying pen info
print(pen1.get_info())

# Refilling the pen
pen1.refill()

# Writing again after refilling
pen1.write("Writing after refill")

class Car:
    def __init__(self, make, model, year, color):
        """Initialize the car with make, model, year, and color."""
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False

    def start(self):
        """Start the car."""
        if not self.is_running:
            self.is_running = True
            print(f"The {self.color} {self.year} {self.make} {self.model} is now running.")
        else:
            print(f"The car is already running.")

    def stop(self):
        """Stop the car."""
        if self.is_running:
            self.is_running = False
            print(f"The {self.color} {self.year} {self.make} {self.model} has stopped.")
        else:
            print(f"The car is already stopped.")

    def paint(self, new_color):
        """Change the color of the car."""
        old_color = self.color
        self.color = new_color
        print(f"The car has been repainted from {old_color} to {new_color}.")

    def __str__(self):
        """Return a string representation of the car."""
        return f"{self.year} {self.make} {self.model} ({self.color})"


# Example usage
if __name__ == "__main__":
    # Create a Car object
    my_car = Car(make="Toyota", model="Camry", year=2022, color="red")

    # Display the car's details
    print(my_car)

    # Start the car
    my_car.start()

    # Try starting it again
    my_car.start()

    # Change the color
    my_car.paint("blue")

    # Stop the car
    my_car.stop()

    # Try stopping it again
    my_car.stop()

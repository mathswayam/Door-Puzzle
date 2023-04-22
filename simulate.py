import random

# Define a class for the rotating door with switches
class RotatingDoor:
    def __init__(self):
        self.switches = [random.choice([True, False]) for _ in range(4)]  # random initial state of switches
        self.is_open = False  # door is initially closed
        self.prev_button_position = None  # no previous button position
        
    def try_combination(self):
        # check if all switches are off
        if all(not switch for switch in self.switches):
            self.is_open = True  # door opens if all switches are off
            print("Door opened!")
            return True
        else:
            # door rotates in a high speed and switches positions
            print("Door rotates in a high speed!")
            self.rotate_switches()
            return False
            
    def rotate_switches(self):
        # randomly choose a new position for the previous button
        new_button_position = random.randint(0, 3)
        while new_button_position == self.prev_button_position:
            new_button_position = random.randint(0, 3)
        # compute the new position of the buttons after the door rotates
        new_switches = self.switches[new_button_position:] + self.switches[:new_button_position]
        self.switches = new_switches
        self.prev_button_position = new_button_position
        print(f"Previous button position: {self.prev_button_position}")
        print(f"New switches positions: {self.switches}")
            
    def simulate_test(self, num_buttons, button_positions=None):
        no_buttons=button_positions
        if button_positions is None:
            # choose random button positions if none are given
            button_positions = random.sample(range(4), num_buttons)
        elif len(button_positions) != num_buttons:
            # raise an error if the number of button positions does not match num_buttons
            raise ValueError("The number of button positions does not match num_buttons.")
        
        attempts = 0
        while not self.try_combination():
            attempts += 1
            if no_buttons is None:
                button_positions = random.sample(range(4), num_buttons)  # choose new random positions at each attempt
            # press the buttons at the specified positions
            for button_position in button_positions:
                self.switches[button_position] = not self.switches[button_position]
                print(f"Button {button_position+1} pressed. New state: {self.switches[button_position]}")
                
        return attempts
    
    def print_switches_state(self):
        print("Current switches state:", self.switches)

# Simulate and print the number of attempts for all 7 conditions
door = RotatingDoor()

print("\n Press a single button at given position")
attempts = door.simulate_test(1, [0])
door.print_switches_state()
print(f"The door opened after {attempts} attempts")

# print("\n Press a single button at a random position")
# attempts = door.simulate_test(1)
# door.print_switches_state()
# print(f"The door opened after {attempts} attempts")

# print("\n Press two buttons at given position")
# attempts = door.simulate_test(2, [0,1])
# door.print_switches_state()
# print(f"The door opened after {attempts} attempts")

# print("\n Press two buttons at random positions")
# attempts = door.simulate_test(2)
# door.print_switches_state()
# print(f"The door opened after {attempts} attempts")

# print("\n Press three buttons at given positions")
# attempts = door.simulate_test(3, [0,1,2])
# door.print_switches_state()
# print(f"The door opened after {attempts} attempts")

# print("\n Press three buttons random positions")
# attempts = door.simulate_test(3)
# door.print_switches_state()
# print(f"The door opened after {attempts} attempts")

# print("\n Press four buttons")
# attempts = door.simulate_test(4,[0,1,2,3])
# door.print_switches_state()
# print(f"The door opened after {attempts} attempts")


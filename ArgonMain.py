# Argon V1.0 Prebuild


# IMPORTED LIBARIES
import random
import string
import turtle
import time

# Master Mode
ModeController=6
# 1 = Basic Scearch Engine
# 2 = Time Checker
# 3 = Codemaker
# 4 = Buffer
# 5 = Sun Maker
# 6 = Timer





if ModeController == 1:
# Simulated search engine responses
 responses = {
    "dog": {
        "wikipedia": "https://en.wikipedia.org/wiki/Dog",
        "images": ["https://...", "..."],
        "videos": ["https://...", "..."],
    },
    "cat": {
        "wikipedia": "https://en.wikipedia.org/wiki/Cat",
        "images": ["https://...", "..."],
        "videos": ["https://...", "..."],
    },
    # Add more prompts and responses here
 }

 def search(prompt):
  """Simulates a search engine by returning predefined responses."""
  prompt = prompt.lower()
  if prompt in responses:
    return responses[prompt]
  else:
    return f"Sorry, I couldn't find anything related to '{prompt}'."

 # Get user input
 prompt = input("Search for something: ")

 # Simulate search and display results
 results = search(prompt)
 if results:
  print(f"Wikipedia: {results['wikipedia']}")
  print("Images:")
  for image in results["images"]:
    print(f"- {image}")
  print("Videos:")
  for video in results["videos"]:
    print(f"- {video}")
 else:
  print(results)

 print("Remember, this is just a sample script. Real search engines access and process vast amounts of information from the internet.")

if ModeController == 2:
  from datetime import datetime

 # Get the current date and time
  now = datetime.now()

 # Format the date and time in a user-friendly way
  current_time = now.strftime("%H:%M:%S")

 # Print the current time to the console
  print(f"The current time is: {current_time}")

if ModeController == 3:
 
 # Define all possible characters
 chars = string.ascii_letters + string.digits + string.punctuation

 # Generate a random string length between 10 and 20 characters
 string_length = random.randint(10, 20)

 # Generate the random string
 random_string = ''.join(random.choice(chars) for i in range(string_length))

 # Print the random string
 print(random_string)

if ModeController == 4:
 buffer = 0  # Initialize buffer to 0

 user_input = input("Would you like to enter a starting value for the buffer? Enter 'yes' or 'no': ")
 if user_input.lower() == "yes":
  try:
   buffer = int(input("Enter a starting value for the buffer: "))
  except ValueError:
   print("Invalid input. Please enter a whole number.")
   buffer = 0  # Reset buffer to 0 if invalid input

 # Get the loop range from the user
 loop_range = input("Enter the number of times you want the loop to run: ")
 try:
  loop_range = int(loop_range)
 except ValueError:
  print("Invalid input. Loop range will be set to 10.")
  loop_range = 10

 # Loop through the specified range
 for i in range(loop_range):
  buffer += 20  # Add 20 to buffer
  print(buffer)  # Print the updated buffer value

if ModeController == 5:
 # Set up the turtle screen
 screen = turtle.Screen()
 screen.setup(width=400, height=300)

 # Define the function to draw a smiling sun
 def draw_sun(x, y, radius, color):
   # Create a turtle for the sun
   sun = turtle.Turtle()
   sun.speed(0)  # Set the turtle's speed to fastest
   sun.penup()  # Lift the pen to avoid drawing lines
   sun.goto(x, y)  # Move the turtle to the desired position
   sun.pendown()  # Put the pen down to start drawing

   # Draw the sun's face
   sun.fillcolor(color)
   sun.begin_fill()
   sun.circle(radius)
   sun.end_fill()

   # Draw the eyes
   eye_radius = radius / 5
   sun.penup()
   sun.goto(x - radius / 3, y + radius / 3)
   sun.pendown()
   sun.dot(eye_radius, "black")
   sun.penup()
   sun.goto(x + radius / 3, y + radius / 3)
   sun.pendown()
   sun.dot(eye_radius, "black")

   # Draw the smile
   sun.penup()
   sun.goto(x - radius / 3, y - radius / 3)
   sun.pendown()
   sun.setheading(-60)  # Set the heading for the smile
   sun.circle(radius / 3, 120)  # Draw a 120-degree arc for the smile

   # Hide the turtle
   sun.hideturtle()

 # Draw multiple smiling suns
 num_suns = 10
 for _ in range(num_suns):
   x = random.randint(-200, 200)  # Random x-coordinate within screen boundaries
   y = random.randint(-150, 150)  # Random y-coordinate within screen boundaries
   radius = random.randint(20, 50)  # Random radius
   color = random.choice(["yellow", "orange", "gold"])  # Random color
   draw_sun(x, y, radius, color)

 # Keep the window open until closed manually
 turtle.done()

if ModeController == 6:
 for seconds in range(1, 11):  # Loop from 1 to 10
    print(f"Time passed: {seconds} seconds")
    time.sleep (1)

 if ModeController == 6:
 # Create the screen and set the background color
  screen = turtle.Screen()
 screen.bgcolor("lightblue")

 # Draw the planet
 planet = turtle.Turtle()
 planet.penup()
 planet.goto(0, -100)
 planet.pendown()
 planet.fillcolor("lightgreen")
 planet.begin_fill()
 planet.circle(50)
 planet.end_fill()

 # Draw more mountains with a loop
 num_mountains = 5
 for i in range(num_mountains):
  mountain = turtle.Turtle()
  mountain.penup()
  mountain.goto(-150 + (60 * i), -50)  # Adjust spacing as needed
  mountain.pendown()
  mountain.fillcolor("gray")
  mountain.begin_fill()
  mountain.left(140)
  mountain.forward(100)
  mountain.right(120)
  mountain.forward(100)
  mountain.right(120)
  mountain.forward(100)
  mountain.end_fill()

 # Draw more trees with a loop
 num_trees = 8
 for i in range(num_trees):
  tree = turtle.Turtle()
  tree.penup()
  tree.goto(-120 + (60 * i), 0)  # Adjust spacing and positioning as needed
  tree.pendown()
  tree.fillcolor("brown")
  tree.begin_fill()
  tree.left(90)
  tree.forward(20)
  tree.right(90)
  tree.forward(10)
  tree.right(90)
  tree.forward(20)
  tree.left(90)
  tree.forward(10)
  tree.end_fill()

  tree.penup()
  tree.goto(-120 + (60 * i), 20)
  tree.pendown()
  tree.fillcolor("green")
  tree.begin_fill()
  tree.circle(15)
  tree.end_fill()

 # Keep the window open until closed manually
 turtle.done()

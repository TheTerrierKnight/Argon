# Argon V1.0 Prebuild
#Careful when using!


# IMPORTED LIBARIES



# Master Mode
ModeController=2
# 1 = Basic Scearch Engine





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

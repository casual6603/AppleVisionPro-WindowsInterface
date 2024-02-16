import time

def reset_starting_x():
  global starting_x
  starting_x = time.time()  # Update starting time

# Initialize starting_x
starting_x = time.time()

while True:
  # Do something with starting_x (replace with your actual logic)
  print(f"Current time: {time.time()}")
  print(f"Starting time (starting_x): {starting_x}")

  # Check if 5 seconds have passed
  if time.time() - starting_x >= 5:
    reset_starting_x()

  # Sleep for a short duration to avoid busy waiting
  time.sleep(0.1)

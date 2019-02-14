import pygame
from itertools import product

pygame.init()

# config
stop_flag = "[[:stop:]]"

def text_to_binary(text):
  '''
  Converts ASCII text to a string binary digits. Each character will be
  represented as 8 bits.
  '''

  binary_str = ""
  
  for c in text:
    d = ord(c)
    b = bin(d)
    b = b[2:]

    while len(b) < 8:
      b = "0" + b
    
    binary_str += b
    
  return binary_str

def binary_to_text(binary_str):
  '''
  Converts a string binary digits to ASCII text. Each character will be
  represented as 8 bits.
  '''

  result = ""

  # separate binary string into 8 bit chunks
  chunks = [binary_str[i: i+8] for i in range(0, len(binary_str), 8)]

  for c in chunks:
    d = int(c, 2)
    if d <= 126:
      result += str(chr(d))

  return result

def hide_message(message_file_path, original_image_path, encoded_image_path):
  '''
  Hides a secret message inside an image file.
  '''

  # read message from text file and append stop flag
  with open(message_file_path, 'r') as f:
    message = f.read()
  message += stop_flag

  # convert message to binary
  binary_str = text_to_binary(message)
    
  # load the original image file as a surface
  surf = pygame.image.load(original_image_path)
  width = surf.get_width()
  height = surf.get_height()

  # loop through message and adjust pixels
  i = 0
  x = 0
  y = 0 
      
  while i < len(binary_str):
    loc = [x, y]
    color = surf.get_at(loc)

    blue = color.b
    bit = int(binary_str[i])
    even = blue % 2 == 0
        
    if (even and bit == 1) or (not even and bit == 0):
      blue += 1

      if blue > 255:
        blue -= 2
        
      color.b = blue
    
      surf.set_at(loc, color)
    
    i += 1
    x += 1

    if x == width:
      x = 0
      y += 1
    
  # save the new image
  pygame.image.save(surf, encoded_image_path)

  print("Success! Your secret message was hidden in '" + encoded_image_path + "'.")


def extract_message(encoded_image_path, extracted_message_path):
  '''
  Extracts a secret message from an image file.
  '''

  # load image as surface
  surf = pygame.image.load(encoded_image_path)
  width = surf.get_width()
  height = surf.get_height()

  # build binary digit string from image
  binary_str = ""
  
  for y in range(height):
    for x in range(width):
      loc = [x, y]
      color = surf.get_at(loc)
      blue = color.b
      binary_str += str(blue % 2)

  # convert binary string to text
  message = binary_to_text(binary_str)
  
  # truncate any characters after stop flag
  end = message.find(stop_flag)
  message = message[:end]
  
  # write extracted message to file
  with open(extracted_message_path, 'w') as f:
    f.write(message)
        
  print("Success! Your secret message was extracted to '" + extracted_message_path + "'.")

extract_message('blocklife start screen.png', 'answer_file')

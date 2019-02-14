# Blue Steganography

## About

Steganography is the practice of concealing information within other nonsecret text or data. This program hides text messages inside image files. It works as follows:

Each character in a message is converted to an 8-bit binary value based on its ASCII value. The 8 bits are saved into an image within the blue component of consecutive pixels. If a bit is a 0, then the blue component of the RGB color for a pixel is adjusted by no more than one so that it is even. If a bit is a 1, then the blue component color is adjusted to be odd. Since the color adjustments are so small, the resulting image should be virtually identical to the same image without an embedded image.

To extract a message, simply read an image file 8 pixels at a time where even blue values are a 0 and odds are a 1. Then convert each binary value back to its corresponding ASCII character.

The great thing about this encryption technique is that two people can communicate without any direct line of communication! For example, just hide messages inside memes on an image sharing site. Most people will just see the meme and not know anything secret is inside. However, your partner can download the same image and extract the secret message.

## Hiding messages

To embed a message,

  1) Import blue_steganography.
  2) Type a message in a plain text file.
  3) Set the path to the message file.
  4) Set the path to original image in which message will be hidden. The file type must be a PNG or Bitmap image*. This image will not be altered.
  5) Set the path to new image in which message will be hidden. The file type must also be a PNG or Bitmap image. This image will be created when the message is hidden.
  6) Call hide_message()

\* JPEG images are not supported because of the way JPEG file compression works. Only image formats that preserve the exact color value for every pixel can be used with this technique.

Example usage:

```
message_file = "path/to/secret.txt"
original_image = "path/to/image1.png"
encoded_image =  "path/to/image2.png"
blue_steganography.hide_message(message_file, original_image, encoded_image)
```

## Extracting messages

To extract a message,

  1) Import blue_steganography.
  2) Set the path to image in which message is hidden.
  3) Set the path to the text file in which the extracted message will be saved.
  4) Call extract_message()
  5) Open the newly created text file to read the message.

Example Usage:

```
encoded_image =  "path/to/image2.png"
extracted_message = "path/to/some_file.txt"
blue_steganography.extract_message(encoded_image, extracted_message)
```

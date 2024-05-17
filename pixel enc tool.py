from PIL import Image

def encrypt_decrypt(image_path, key, mode):
 
  img = Image.open(image_path)
  pixels = img.load()
  width, height = img.size


  for y in range(height):
    for x in range(width):
      red, green, blue = pixels[x, y]
      new_red = red ^ key if mode == "encrypt" else red ^ key
      new_green = green ^ key if mode == "encrypt" else green ^ key
      new_blue = blue ^ key if mode == "encrypt" else blue ^ key
      pixels[x, y] = (new_red, new_green, new_blue)

 
  img.save(f"{image_path[:-4]}_{mode}.png") 


image_path = input("Enter the image path: ")
key = int(input("Enter the secret key (integer): "))
mode = input("Enter 'encrypt' or 'decrypt': ")

if mode not in ["encrypt", "decrypt"]:
  print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
  exit()

encrypt_decrypt(image_path, key, mode)
print(f"Image {mode}ed successfully!")

from PIL import Image
import os
import matplotlib.pyplot as plt

######## Stage I
def rename_image(source_file, destination_directory, newName):
    if os.path.isfile(source_file):
        image = Image.open(source_file)
        file_name = os.path.basename(source_file)
        destinationpath = os.path.join(destination_directory, newName)
        image.save(destinationpath)
        print(f"File {file_name} renamed to {newName} and saved in {destinationpath}")
    else:
        print("Source file not found.")
        return None

####### Stage II
### a)
def horizontal_mirroring(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)

def vertical_mirroring(image):
    return image.transpose(Image.FLIP_TOP_BOTTOM)

### b)
def convert_grayscale(image):
    return image.convert("L")

### c)

def quantization(image_tons_de_cinza, n):
    if n >= 256:
        return image_grayscale  

    tb = 256 / n
    quantized_image  = Image.new("L", image_tons_de_cinza.size)

    for x in range(image_tons_de_cinza.width):
        for y in range(image_tons_de_cinza.height):
            pixel_valor = image_tons_de_cinza.getpixel((x, y))
            bin_idx = int(pixel_valor / tb)
            pixel_quantizado = int((bin_idx + 0.5) * tb)
            quantized_image .putpixel((x, y), pixel_quantizado)

    return quantized_image 
#####################################################################################################
if __name__ == "__main__":
    source_file = "C:/Users/example/Desktop/name/image_example.jpg"   ## put the source file path here
    destination_directory = "C:/Users/example/Desktop/name" ## put the file destination path here (where you want to save it)
    newName = "re_recorded_image.jpeg" ## enter the name you want to save the file with and the format you want (.jpg, .jpeg, .png...)
### change "\" to "/" and vice versa on lines 48 and 49 if it breaks when running.

    rename_image(source_file, destination_directory, newName)

    image_original = Image.open(source_file)
    renamed_image = Image.open(os.path.join(destination_directory, newName))

    plt.figure(figsize=(10, 5))  
    plt.subplot(1, 2, 1)  
    plt.imshow(image_original)
    plt.title("Original Image")

    plt.subplot(1, 2, 2)  
    plt.imshow(renamed_image)
    plt.title("re-recorded image")
    plt.show()
    
    image_horizontal = horizontal_mirroring(image_original)
    image_horizontal.show()
    
    image_vertical = vertical_mirroring(image_original)
    image_vertical.show()

    image_original = Image.open(source_file)
   
    image_grayscale = convert_grayscale(image_original)
    image_grayscale .show()

    number_shades = 6  
    quantized_image  = quantization(image_grayscale, number_shades)
    quantized_image .show()

#### d)
    file_name_resultante = "imagem_resultante.jpeg"
    resulting_path = os.path.join(destination_directory, file_name_resultante)
    quantized_image .save(resulting_path)
    print(f"Quantized image saved in {resulting_path}")

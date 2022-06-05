from PIL import Image

# List of ascii characters:
# asciiChars = [ 'A', 'B','C','D','E', 'F','G','H','I','J','K','L','M','N', 'S','@','#','%','?','*','+',';',':',',','.']
asciiChars = [ 'S','@','#','%','?','*','+',';',':',',','.']
# print(len(asciiChars))

# Convert image to grayscale:
def imageToGrayscale(image):
    return image.convert('L')

# Convert grayscale image to ascii:
def grayscaleToAscii(grayscaleImage):
    pixels = grayscaleImage.getdata()
    # characters = ''.join([asciiChars[pixel // 11] for pixel in pixels])
    characters = ''.join([asciiChars[pixel // 25] for pixel in pixels])
    return characters.lower()

def resizeImage(image, modifiedWidth):
    width, height = image.size
    ratio = height/width
    modifiedHeight = int(modifiedWidth * ratio)
    return image.resize((modifiedWidth, modifiedHeight))

def main(modifiedWidth = 200):
    path = './source/sunflower.png'
    # path = '/Users/arpanagarwal/Desktop/me.jpg'
    # path = input("Enter the image path:\n")
    try:
        image = Image.open(path)
    except:
        print(path, ' is not a valid pathname to an image.')
        return
    image = Image.open(path)
    newImageData = grayscaleToAscii(imageToGrayscale(resizeImage(image, modifiedWidth)))
    numPixels = len(newImageData)
    asciiImage = "\n".join([newImageData[index:(index+modifiedWidth)] for index in range(0, numPixels, modifiedWidth)])

     # print result
    # print(asciiImage)
    
    # save result to "ascii_image.txt"
    with open('./out/ascii_image.txt', 'w') as f:
        f.write(asciiImage)

main()
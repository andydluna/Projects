from PIL import Image

def resized_image(size1, size2):
    image = Image.open("data\emumu.jpeg")

    print(f'Current size: {image.size}')

    resized_image = image.resize((size1, size2))

    resized_image.save('data\emumu-' + str(size1) + '-' + str(size2) + '.jpeg')

size1 = int(input('Enter width: '))
size2 = int(input('Enter Length: '))
resized_image(size1, size2)
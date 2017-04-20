from PIL import Image

# im = Image.open('quickpass-logo.png')


with open('quickpass-logo.png','rb') as b:
    x = b.read()
    print(b.read())


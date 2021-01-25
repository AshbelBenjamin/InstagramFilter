def setup():
    size(700,500)

    img = loadImage("Space.jpg")
    image(img,0,0,811,609)

    # NYCImg = loadImage("NYC.jpg")
    # image(NYCImg,0,0, 4032, 1720)

def draw():

    loadPixels()
    updatePixels()

def mousePressed(): #press mouse to make blue and green
    
    loadPixels()

    for i in range(len(pixels)):
     old = pixels[i]
     pixels[i] = color(0, green(old), blue(old))
    
    updatePixels()
    
def keyPressed(): #press key to make grey
    
    loadPixels()

    for i in range(len(pixels)):
        old = pixels[i]
        avg = (red(old) + green(old) + blue(old)) / 3
        pixels[i] = color(avg)
    
    updatePixels()

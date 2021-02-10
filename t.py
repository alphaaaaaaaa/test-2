from PIL import Image
#Read the two images
image1 = Image.open('qrgenerator/static/cassette_papercraft.png')
image2 = Image.open('qrgenerator/static/test2.png')
#resize, first image

image1_size = image1.size
image2 = image2.resize((200, 200))
image2_size = image2.size

new_image = Image.new('RGB',image1_size)
new_image.paste(image1,(0,0))
new_image.paste(image2,(320,340))
new_image.save("qrgenerator/static/test3.png","JPEG")
new_image.show()
from PIL import Image
ch="yes"
while(ch!="done"):
	try:
		name=input("enter the name of the image you want")
		ext=".jpg"
		path=name+ext
		im=Image.open(path)
		im.show()
		im.close()
	except:
		print("Image not found") 
	ch=input("do you want to open another image")

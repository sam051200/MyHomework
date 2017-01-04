from PIL import Image#要下載PIL(pillow)
f1 = open("test.txt", "w",encoding = 'utf8')#重要
img = Image.open("史迪奇.JPG")
img= img.convert('1') #8位元像素，黑白兩色
print(img.size)
width=100
#height=100
ratio = float(width)/img.size[0]
height = int(img.size[1]*ratio)
nimg = img.resize( (width, height), Image.BILINEAR )
print(nimg.size)
nimg.show()
for y in range(height):
       for x in range(width):
              if(nimg.getpixel((x,y))==0):
                     #print(nimg.getpixel((x,y))," ")
                     print("█",end="",file=f1)
              else:
                     print("  ",end="",file=f1)                
       print("",file=f1)
f1.close()
#img.save("new777.png")

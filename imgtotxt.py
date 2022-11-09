from pywhatkit import image_to_ascii_art as ch        #imprting the function from pywhatkit as ch

# if it shows any error then enter the full path to the file in the string (eg: img1 = 'c:\\user\\Desktop\\doremo.jpg)

img1 = 'doremon.jpg'  
img2 = 'ironman.jpg'
img3 = 'pikachu.png'
img4 = 'name.jpg'
img5 = 'shinchan.png' 
img6 = 'foysl.jpg'
img7 = 'foysal.jpg'

t1 = 'output/t1'
t2 = 'output/t2'
t3 = 'output/t3'
t4 = 'output/name'
t5 = 'output/t5'
t6 = 'output/foysl'
t7 = 'output/foysal'

#converting images into text

ch(img1, t1)  
ch(img2, t2)
ch(img3, t3)
ch(img4, t4)
ch(img5, t5)
ch(img6, t6)
ch(img7, t7)

#
# text_file = open("t6.txt", "r")
# data = text_file.read()
# text_file.close()
#
# print(data)
#printing completed for our conformation..

print('completed... Look output folder.')

from PIL import Image, ImageFilter

image = Image.open("prime-art.png")
# image.show() dosyayı açıyor.
# image.save("a2.png")
# image.rotate(180).save("a3.png")
# image.convert(mode="L").save("a4.png") #siyah-beyaz yapıyor rengi

# boyut = (500,250) # 500,250 verdiğim halde 250x250 olarak fotoğrafı küçülttü, kırpmadı.
# image.thumbnail(boyut)
# image.save("a5.png")

# ImageFilter'ı burası için çağırdık
# image.filter(ImageFilter.GaussianBlur(5)).save("a6.png")

#kirp_alan = (900,0,1700,700) #soldan, yukarıdan, sağdan, aşağıdan
#image.crop(kirp_alan).save("a7")

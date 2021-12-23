print ( "Yemek Tarifi Ödevi " )



yemektarif  =  open (" yemektarifleri.txt" , "w" )
yemektarif . write ( input (   "Yemek adınızı giriniz = " ))
yemektarif . write ( input ( "Yemek tarifi giriniz = " ))
yemektarif . kapat ()
yemektarif = ["", "", ""]

for x in yemektarif:
  print(x)


dosya  =  open ( "yemektarifleri.txt" , "r" )
oku  =  dosya . oku ()
print ( "Yemek Adı ve Tarifi = " , oku )

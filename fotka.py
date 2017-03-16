import os
from PIL import Image

# okreslam moje dane
folder = 'c:\\fotki'
plik = 'DSC07946.JPG'

# tworze bezwzgledna sciezke - c:\\...
sciezka = os.path.join(folder, plik)

# otwieram zdjęcie jako obiekt Image
foto = Image.open(sciezka)

# drujuje kilka wlasciwosci
print(foto.size)
print(foto.format)
print(foto.format_description)
print(foto.width)
print(foto.height)

# zmieniam rozmiar zdjecia - resize() zwraca nowy obiekt Image
# musze wiec zapisac go do zmiennej, pamietam o zaokragleniu do calych pikseli
nowy = foto.resize(( round(foto.width/2), round(foto.height/2)))
print('Nowy rozmiar:', nowy.size)

# podaje nazwe dla mojego nowego malego zdjecia
nowa_nazwa = 'sredniplik.JPG'

# zapisuje male zdjecie
nowy.save(os.path.join(folder, nowa_nazwa))

# zamykam zdjecie zrodlowe
foto.close()

import os
from PIL import Image

folder = 'c:\\fotki'
plik = 'DSC07946.JPG'

sciezka = os.path.join(folder, plik)

foto = Image.open(sciezka)

# print(foto.size)
# print(foto.format)
# print(foto.format_description)
# print(foto.width)
# print(foto.height)

nowy = foto.resize(( round(foto.width/2), round(foto.height/2)))
print('Nowy rozmiar:',nowy.size)

nowa_nazwa = 'sredniplik.JPG'
nowy.save(os.path.join(folder, nowa_nazwa))

foto.close()

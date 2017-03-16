import os
from PIL import Image

folder = 'c:\\fotki'
root = 'obrazek'

for nr, foto in enumerate(os.listdir(folder)):

    ext = os.path.splitext(foto)[1]

    zdjecie = Image.open(os.path.join(folder, foto))

    ratio = zdjecie.width / zdjecie.height
    nowa_szer = 800
    nowa_wys = round(nowa_szer / ratio)

    male_foto = zdjecie.resize((nowa_szer, nowa_wys))

    nowy_plik = '{}{}{}'.format(root, nr + 1, ext)
    print(nowy_plik)
    
    male_foto.save(os.path.join(folder, nowy_plik))
    print('Zdjecie zapisane:', nowy_plik)

    zdjecie.close()


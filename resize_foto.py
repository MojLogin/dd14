import os

# najpierw musze zainstalowac pakiet Pillow
# pip install Pillow
from PIL import Image


folder = 'c:\\fotki'
root = 'obrazek'
nowa_szer = 800

# w petli otwieram zdjecia, zmieniam ich rozmiar i zapisuje nowe pliki
for nr, foto in enumerate(os.listdir(folder)):
    # biore rozszerzenie z nazwy pliku
    ext = os.path.splitext(foto)[1]
    # otwieram plik zrodlowy
    zdjecie = Image.open(os.path.join(folder, foto))

    # obliczam nowy rozmiar
    ratio = zdjecie.width / zdjecie.height    
    nowa_wys = round(nowa_szer / ratio)
    # tworze male zdjecie
    male_foto = zdjecie.resize((nowa_szer, nowa_wys))
    
    # tworze nazwe dla nowego malego zdjecia
    nowy_plik = '{}{}{}'.format(root, nr + 1, ext)
    print(nowy_plik)
    # zapisuje nowe zdjecie
    male_foto.save(os.path.join(folder, nowy_plik))
    print('Zdjecie zapisane:', nowy_plik)

    zdjecie.close()


from pyembroidery import PyEmbroidery
import os
from converter import Converter
import converter
converter.Converter.saveJson({
    "teste": "teste"
})

path = '.\\files\\folder 452\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))
for f in files:
    if f.split('.')[len(f.split('.'))-1] == 'pes':
        filename = f.split('\\')[len(f.split('\\'))-1]
        try:
            Converter.convertFile(
                f, './imgs/'+filename.replace('.pes', '.png'))
            print(filename)
        except Exception as ex:
            print(ex)

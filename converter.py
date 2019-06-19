from pyembroidery import PyEmbroidery
import io
import json



class Converter(object):
    def convertFile(_from, _to):
        try:
            pattern = PyEmbroidery.read(_from)
            PyEmbroidery.write_png(pattern, _to)
        except Exception as ex:
            print(ex)

    def saveJson(json):
        try:
            with io.open('data.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(json, ensure_ascii=False))
        except Exception as ex:
            print(ex)

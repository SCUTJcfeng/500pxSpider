# python3.6

import csv
import json
import codecs
from threading import Lock


class SaveTool:
    __lock = Lock()

    @staticmethod
    def saveText(data, filename, encoding='utf8', use_lock=False):
        if use_lock:
            SaveTool.__lock.acquire()
            with open(filename, 'w', encoding=encoding) as f:
                f.write(data)
        if use_lock:
            SaveTool.__lock.release()

    @staticmethod
    def saveJson(data, filename, encoding='utf8'):
        SaveTool.saveText(json.dumps(data, indent=4, ensure_ascii=False), filename, encoding)

    @staticmethod
    def saveChunk(r, filename, use_lock=False):
        if use_lock:
            SaveTool.__lock.acquire()
        assert hasattr(r, '__iter__')
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        if use_lock:
            SaveTool.__lock.release()

    @staticmethod
    def saveCSV(data, filename, header, encoding='utf8'):
        with SaveTool.__lock:
            with open(filename, 'wb') as f:
                f.write(codecs.BOM_UTF8)
            with open(filename, 'a', newline='', encoding=encoding) as f:
                writer = csv.DictWriter(f, fieldnames=header)
                writer.writeheader()
                writer.writerows(data)

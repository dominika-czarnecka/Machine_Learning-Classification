import json
import pickle
import os

class SavedClassifiersManager:
    _jsonpath = 'saved\\saved.json'

    @staticmethod
    def delete_all():
        f = json.load(open(SavedClassifiersManager._jsonpath))
        for file in f["files"]:
            os.remove(file["filename"])
        f["files"] = []
        json.dump(f, open(SavedClassifiersManager._jsonpath, 'w'), indent=4)

    @staticmethod
    def add(args, svm):
        new_filename = SavedClassifiersManager._get_filename()
        f = json.load(open(SavedClassifiersManager._jsonpath))
        f["files"].append({"filename": new_filename, "args": args})
        json.dump(f, open(SavedClassifiersManager._jsonpath, 'w'), indent=4)
        pickle.dump(svm, open(new_filename, 'wb'))

    @staticmethod
    def _get_filename():
        i = 0
        while os.path.exists('saved\\clas' + str(i) +'.svm'):
            i += 1
        return 'saved\\clas' + str(i) +'.svm'

    @staticmethod
    def load(args):
        f = json.load(open(SavedClassifiersManager._jsonpath))
        for file in f["files"]:
            if SavedClassifiersManager._dict_equal(args, file['args']):
                return pickle.load(open(file['filename'], 'rb'))
        return None


    @staticmethod
    def _dict_equal(a, b):
        for key in a:
            if a[key] != b[key]:
                return False
        return True
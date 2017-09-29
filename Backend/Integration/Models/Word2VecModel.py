from Backend.Integration.Models.ClassificatorModel import ClassificatorModel


class Word2VecModel(ClassificatorModel):
    def __init__(self, name, path, size, iter, min_count, window):
        self.name = name
        self.path = path
        self.size = size
        self.iter = iter
        self.min_count = min_count
        self.window = window

    @classmethod
    def fromJSON(cls, json_data):
        fromJSON = cls(json_data['name'], json_data['path'], json_data['size'], json_data['iter'], json_data['min_count'], json_data['window'])
        return fromJSON

    def display(self):
        return "name: {}\n" \
               "path: {}\n" \
               "size: {}\n" \
               "iter: {}\n" \
               "min count: {}\n" \
               "window: {}\n".format(self.name, self.path, self.size, self.iter, self.min_count, self.window)

from Backend.Integration.Models.ClassificatorModel import ClassificatorModel


class Word2VecModel(ClassificatorModel):
    def initValues(self, name, path):
        self.name = name
        self.path = path


    def fromJSON(self, json_data):
        self.name = json_data['name']
        self.path = json_data['path']

    def display(self):
        return "name: {}\n" \
               "path: {}\n".format(self.name, self.path)

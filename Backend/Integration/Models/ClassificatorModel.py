import json
import copy


class ClassificatorModel:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __eq__(self, other):
        left = copy.copy(self.__dict__)
        right = copy.copy(other.__dict__)
        left['name'] = ""
        left['path'] = ""
        right['name'] = ""
        right['path'] = ""
        return left == right

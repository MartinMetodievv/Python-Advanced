# from collections import defaultdict
# def start_spring(**spring_object):
#     """
#     This function collects values and their corresponding keys from `spring_object` using defaultdict instead of a regular dictionary.
#     It then sorts the collection based on the length of the values and the keys in descending order.
#     Finally, it returns the sorted collection as a formatted string.
#     """
#     collection = defaultdict(list)
#     result = ''
#     for k, v in spring_object.items():
#         collection[v].append(k)
#     collection = dict(sorted(collection.items(), key=lambda x: (-len(x[1]), x[0])))
#
#     for key, value in collection.items():
#         result += f'{key}:\n'
#         for x in sorted(value):
#             result += f'-{x}\n'
#     return result
from _collections import defaultdict


class StartSpring:
    def __init__(self, **kwargs):
        self.items = kwargs
        self.data = defaultdict(list)
        self.sorted_data = {}
        self.message = ''

    def process_initial_data(self):
        for item_name, item_type in self.items.items():
            self.data[item_type].append(item_name)

    def sort_data(self):
        self.sorted_data = dict(sorted(self.data.items(), key=lambda x: (-len(x[1]), x[0],)))

    def prepare_output_message(self):
        for k, v in self.sorted_data.items():
            self.message += f'{k}:\n'
            for x in sorted(v):
                self.message += f'-{x}\n'
        # return self.message

    def __repr__(self):
        return self.message


def start_spring(**kwargs):
    output = StartSpring(**kwargs)
    output.process_initial_data()
    output.sort_data()
    output.prepare_output_message()
    return f'{output}'


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))

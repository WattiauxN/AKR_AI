import inspect

class Dumper:
    def __init__(self):
        pass

    def print_dump(self, obj): 
      # https://stackoverflow.com/questions/192109/is-there-a-built-in-function-to-print-all-the-current-properties-and-values-of-a
      # https://gist.github.com/passos/1071857
      for attr in dir(obj):
        print("obj.%s = %r" % (attr, getattr(obj, attr)))
    
    def dump(self, obj):
        res = []
        for attr in dir(obj):
            res.append("%r" % (getattr(obj, attr)))
        return res
    
    def get_instance_method(self, obj):
        res = self.dump(obj)
        for i in res:
            if "bound method" not in i: 
                continue
            else:
                print(i)

    def dump_methods(self, cls):
        # Get all members of the class
        members = inspect.getmembers(cls, predicate=inspect.isfunction)
        # Filter out dunder methods
        filtered_methods = {name: method for name, method in members if not name.startswith('__')}
        return filtered_methods

    def dump_attributes(self, obj):
        # Get all attributes from the object's __dict__
        attributes = vars(obj)  # or obj.__dict__
        # Filter out dunder methods and attributes
        filtered_attributes = {key: value for key, value in attributes.items() if not key.startswith('__') or not key.endswith('__')} 
        return filtered_attributes
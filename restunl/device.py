class Device(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return type(self).__name__ + '(' + self.name + ')'

    def to_json(self):
        return self.__dict__


class Router(Device):
    defaults = {
        'template': 'vios',
        'count': 1,
        'image': 'vios-adventerprisek9-m.virl.154-2.T1',
        'ram': '512',
        'ethernet': '4',
        'serial': '0',
        'type': 'vios',
        'config': 'unconfigured'
    }

    def __init__(self, name):
        for key, value in Router.defaults.items():
            setattr(self, key, value)
        super(Router, self).__init__(name)

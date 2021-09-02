def build_filter(args):
    return Filter(args)

class Filter():
    def __init__(self, args):
        pass

    def file_data_filter(self,file_data):
        file_ctx = file_data['file_ctx']
        filename = file_data['filename']
        if 'tests/data/' in str(filename):
            file_data['file_ctx'] = None
            file_data['filename'] = None

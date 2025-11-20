import os

class Extractor():
    # extracts to Excel
    def __init__(self, default_template_path=os.path.join(os.getcwd(), 'template.xlsx')):
        self.template = self._load_default_template(default_template_path)

    def _load_default_template(self, path):
        if os.path.exists(path):
            #open template here
            return
        raise FileNotFoundError('Default template not found')

    def write_data(self, data):
        pass

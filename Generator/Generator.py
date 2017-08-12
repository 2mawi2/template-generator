from Generator.FileIO import FileIO
from Generator.Template import Template


class Generator:
    def __init__(self, templates: [Template]):
        self.templates = templates

    def generate(self):
        for t in self.templates:
            self.__validate_template(t)
            self.__create_file_from_template(t)

    @staticmethod
    def __validate_template(t: Template):
        if not FileIO.exists(t.template_uri):
            raise FileNotFoundError(t.template_uri)
        if FileIO.exists(t.output_uri):
            raise FileExistsError(t.output_uri)

    @staticmethod
    def __create_file_from_template(t: Template):
        content = FileIO.read(t.template_uri)
        for key, value in t.replacers.items():
            content = content.replace(key, value)
        FileIO.write(t.output_uri, content)

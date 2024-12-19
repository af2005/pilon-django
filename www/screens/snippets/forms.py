from django.template import loader


class Textfield():
    def __init__(self, name, label):
        super().__init__()
        self.name = name
        self.label = label

    def render(self):
        return loader.get_template('www/snippets/forms/long-text-field.html').render({
            "name": self.name,
            "label": self.label
        })


class SubmitButton:
    def __init__(self, text):
        self.text = text

    def render(self):
        return loader.get_template('www/snippets/forms/submit-button.html').render({
            "text": self.text
        })



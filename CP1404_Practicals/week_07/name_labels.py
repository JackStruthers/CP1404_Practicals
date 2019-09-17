from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class LabelPractice(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ("John", "Jack", "Yasmin", "Brad")

    def build(self):
        self.title = "Label list practice"
        self.root = Builder.load_file('name_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.names_box.add_widget(temp_label)


LabelPractice().run()

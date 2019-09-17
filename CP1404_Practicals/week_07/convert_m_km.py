from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILE_TO_KM = 1.60934


class ConvertMilesToKilometers(App):

    def build(self):
        Window.size = (600, 500)
        self.title = "Convert Miles to Kilometers!"
        self.root = Builder.load_file('convert_m_km.kv')

    def handle_conversion(self):
        miles = self.error_check_miles()
        result = MILE_TO_KM * miles
        self.root.ids.output_km.text = str(result)

    def handle_button_change(self, change):
        miles = self.error_check_miles()
        result = miles + change
        self.root.ids.input_miles.text = str(result)

    def error_check_miles(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            return miles

        except ValueError:
            return 0


ConvertMilesToKilometers().run()


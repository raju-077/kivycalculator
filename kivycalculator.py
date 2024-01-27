from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.size = (500, 700)
Builder.load_file('my.kv')
class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button):
        prior = self.ids.calc_input.text

        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'

        else:
            self.ids.calc_input.text = f'{prior}{button}'
    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def dot(self):
        prior = self.ids.calc_input.text
        if "." in prior:
            pass
        else:
           prior = f'{prior}.'
           self.ids.calc_input.text =prior


    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'
       

    def equal(self):
        prior = self.ids.calc_input.text

        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            for number in num_list:
                answer = answer +  int(number)
            self.ids.calc_input.text = str(answer)




class Awesome(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    Awesome().run()
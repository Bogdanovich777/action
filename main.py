from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

class QuestGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.story = {
            "start": {
                "text": "Оля решила стать визажистом, чтобы стать известной и заработать миллионы. Она записалась на курсы макияжа. Что она сделает в первую очередь?",
                "image": "images/start.png",
                "choices": {
                    "Купить кисти и косметику": "buy_tools",
                    "Посмотреть урок на YouTube": "watch_tutorial"
                }
            },
            "buy_tools": {
                "text": "Оля купила самые дорогие кисти и косметику, но перепутала средства и сделала себе странный грим. Что дальше?",
                "image": "images/buy_tools.png",
                "choices": {
                    "Попробовать снова": "retry_makeup",
                    "Идти на курсы с этим макияжем": "go_to_course"
                }
            },
            "watch_tutorial": {
                "text": "Оля нашла блогера, который делал макияж на арбузе. Она вдохновилась и решила повторить. Что дальше?",
                "image": "images/watch_tutorial.png",
                "choices": {
                    "Попробовать на себе": "retry_makeup",
                    "Идти на курсы без практики": "go_to_course"
                }
            },
            "retry_makeup": {
                "text": "Оля повторила попытку, но её макияж снова напоминал что-то из научной фантастики. Она все равно решила пойти на курсы. Что дальше?",
                "image": "images/retry_makeup.png",
                "choices": {
                    "Идти на курсы с этим макияжем": "go_to_course"
                }
            },
            "go_to_course": {
                "text": "На курсах Оля встретила Олега, который пришел, чтобы научиться макияжу для работы в кино. Что дальше?",
                "image": "images/go_to_course.png",
                "choices": {
                    "Похвастаться своими кистями": "show_off",
                    "Попросить у Олега помощи": "ask_for_help"
                }
            },
            "show_off": {
                "text": "Оля показала свои дорогие кисти, но уронила их все на пол. Олег помог собрать их и предложил попробовать другой способ. Они вместе начали работать над макияжем.",
                "image": "images/show_off.png",
                "choices": {
                    "Продолжить работать с Олегом": "happy_end"
                }
            },
            "ask_for_help": {
                "text": "Олег показал Оле, как сделать идеальный макияж. Она была в восторге от его мастерства и пригласила его на кофе после курсов.",
                "image": "images/ask_for_help.png",
                "choices": {
                    "Пойти на кофе с Олегом": "happy_end"
                }
            },
            "happy_end": {
                "text": "Оля и Олег стали лучшей парой визажистов в городе. Они открыли свою студию и жили счастливо вместе.",
                "image": "images/happy_end.png",
                "choices": {}
            }
        }

        self.current_scene = 'start'

        self.image = Image(source=self.story[self.current_scene]['image'], allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(self.image)

        self.text_label = Label(text=self.story[self.current_scene]['text'], halign='center', valign='middle', font_size='18sp', size_hint_y=0.25)
        self.text_label.bind(size=self.text_label.setter('text_size'))
        self.add_widget(self.text_label)

        self.button_layout = BoxLayout(size_hint_y=None, height=50)
        self.add_widget(self.button_layout)
        self.update_choices()

    def update_choices(self):
        self.button_layout.clear_widgets()
        choices = self.story[self.current_scene]['choices']
        for choice, next_scene in choices.items():
            button = Button(text=choice)
            button.bind(on_press=lambda instance, ns=next_scene: self.change_scene(ns))
            self.button_layout.add_widget(button)

    def change_scene(self, next_scene):
        self.current_scene = next_scene
        self.text_label.text = self.story[self.current_scene]['text']
        self.image.source = self.story[self.current_scene]['image']
        self.update_choices()

class QuestApp(App):
    def build(self):
        return QuestGame()

if __name__ == '__main__':
    QuestApp().run()

from mycroft import MycroftSkill, intent_file_handler


class OrderrFood(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('food.orderr.intent')
    def handle_food_orderr(self, message):
        self.speak_dialog('food.orderr')


def create_skill():
    return OrderrFood()


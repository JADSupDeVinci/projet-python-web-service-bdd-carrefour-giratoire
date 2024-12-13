from database import Color, DragonType, Element, Environment, SpecialFeature
import random

class RandomDragon:
    color: str
    dragon_type: str
    element: str
    environment: str
    special_feature: str


    def __init__(self):
        self.color = random.choice(Color.get_all_color())
        self.color = self.color.color_name

        self.dragon_type = random.choice(DragonType.get_all_dragon_types())
        self.dragon_type = self.dragon_type.type_name

        self.element = random.choice(Element.get_all_elements())
        self.element = self.element.element_name

        self.environment = random.choice(Environment.get_all_environments())
        self.environment = self.environment.environment_name

        self.special_feature = random.choice(SpecialFeature.get_all_special_features())
        self.special_feature = self.special_feature.feature_name

    def toDict(self):
        return {
            "Dragon Name": f"Le {self.dragon_type} {self.element} {self.color}, {self.special_feature}, {self.environment}.",
            'Color': self.color,
            'Dragon Type': self.dragon_type,
            'Element': self.element,
            'Environment': self.environment,
            'Special Feature': self.special_feature
        }
import file_operations
from faker import Faker
from random import *
import os

fake = Faker("ru_RU")
skills = ['Стремительный прыжок', 'Электрический выстрел', 'Ледяной удар', 'Стремительный удар', 'Кислотный взгляд', 'Тайный побег', 'Ледяной выстрел', 'Огненный заряд']
letters_mapping = {
	'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

skills = sample(skills, 3)
skill_1 = skills[0]
skill_2 = skills[1]
skill_3 = skills[2]

result = 'cards/result.svg'
cards = os.path.dirname(result)
os.makedirs(cards, exist_ok=True)

def get_runic_skill(skill):
	for char in skill:
		skill = skill.replace(char, letters_mapping[char])
	return skill

for i in range(1, 11):
	context = {
		"first_name": fake.first_name(),
  		"last_name": fake.last_name(),
  		"job": fake.job(),
  		"town": fake.city(),
 		"strength": randint(3, 18),
 		"agility": randint(3, 18),
  		"endurance": randint(3, 18),
  		"intelligence": randint(3, 18),
  		"luck": randint(3, 18),
  		"skill_1": get_runic_skill(skill_1),
  		"skill_2": get_runic_skill(skill_2),
  		"skill_3": get_runic_skill(skill_3)
  	}
	result = f'cards/result{i}.svg'
	file_operations.render_template("charsheet.svg", result, context)

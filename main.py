def create_pet_dict():
  pets = {}
  pet_name = input("Введите имя питомца: ")
  pet_species = input("Введите вид питомца: ")
  pet_age = int(input("Введите возраст питомца: "))
  owner_name = input("Введите имя владельца: ")

  # Определяем правильное окончание для возраста
  if 10 <= pet_age % 100 <= 20:
      age_suffix = "лет"
  else:
      age_suffix = "год" if pet_age % 10 == 1 else "года" if pet_age % 10 in [2, 3, 4] else "лет"

  pets[pet_name] = {
      'Вид питомца': pet_species,
      'Возраст питомца': pet_age,
      'Имя владельца': owner_name
  }

  print(f"Это {pets[pet_name]['Вид питомца']} по кличке \"{pet_name}\". "
        f"Возраст питомца: {pet_age} {age_suffix}. "
        f"Имя владельца: {owner_name}.")

  return pets

def create_power_dict():
  my_dict = {i: i ** i for i in range(10, -6, -1)}
  return my_dict

# Запускаем функции
pets_dict = create_pet_dict()
print(pets_dict)

power_dict = create_power_dict()
print(power_dict)
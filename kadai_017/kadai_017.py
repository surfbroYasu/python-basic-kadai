class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def check_adult(self):
    if self.age >= 20:
      print(f"{self.name}さんは成人です。")
    else:
      print(f"{self.name}さんは未成年です。")

people = [
  Human("佐藤", 18),
  Human("鈴木", 30),
  Human("高橋", 25),
  Human("田中", 12),
  Human("渡辺", 20),
  Human("伊藤", 19),
]

for person in people:
  person.check_adult()


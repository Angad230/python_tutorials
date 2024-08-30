class KeyBoard():
  keyBoardCompany = "Lenovo"
  def __init__(self, favouteKey):
    self.favouteKey = favouteKey

keyboard1 = KeyBoard("Alphabet")
print("keyboard1.keyBoardCompany :",keyboard1.keyBoardCompany)
print("keyboard1.favouteKey: ",keyboard1.favouteKey)
keyboard2 = KeyBoard("Numerical")
print("keyboard2.keyBoardCompany: ",keyboard2.keyBoardCompany)
print("keyboard2.favouteKey: ",keyboard2.favouteKey)
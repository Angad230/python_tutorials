class KeyBoard():
  keyBoardCompany = "Lenovo"
  def __init__(self, numOfKeys,favouteKey):
    
    self.numOfKeys = numOfKeys
    self.favouteKey = favouteKey
  
  def keyBoardDetails(self):
    print(self.favouteKey)
    print(self.numOfKeys)

  @staticmethod
  def totalKeys():
    print("Total number of keys are: 87")

keyboard1 = KeyBoard(5,"Alphabet")
print("keyboard1.keyBoardCompany :",keyboard1.keyBoardCompany)
print("keyboard1.favouteKey: ",keyboard1.favouteKey)
keyboard1.keyBoardDetails()
keyboard1.totalKeys()

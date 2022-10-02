class Location():
   def __init__(self, value_1, dscr, icon):
      self.value_1 = value_1
      self.dscr = dscr
      self.icon = icon
      self.loc_effect_msg = False

class SuperLocation(Location):
   def __init__(self, value_1, value_2, dscr, icon):
      super().__init__(value_1, dscr, icon)
      self.value_2 = value_2

class UltraLocation(SuperLocation):
   def __init__(self, value_1, value_2, value_3, dscr, icon):
      super().__init__(value_1, value_2, dscr, icon)
      self.value_3 = value_3

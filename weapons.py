# Weapons Choice

weapon = raw_input("Which weapon do you weild? \n Sword/Knife/Bow/Axe  ")
if weapon == "sword" or weapon == "Sword":
  # Make a global variable
  weapon = "sword"
  def global_sword():
    global weapon
    weapon = "sword"
  global_sword()
elif weapon == "knife" or weapon == "Knife":
  weapon = "knife"
  def global_knife():
    weapon = "knife"
  global_knife()
elif weapon == "bow" or weapon == "Bow":
  weapon = "bow"
elif weapon == "axe" or weapon == "Axe":
  weapon = "axe"
else:
  weapon = "weapon"

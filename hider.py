import os


print("\n")

hide_option = input("You want to hide folders and files (y/n) ❔ Or hit Enter to show option !! :")

if(hide_option is ""):
  show_option = input("You want to show folders and files (y/n) ❔ :")

  if(show_option is "y"):
    os.system("attrib -h /s /d")
    print("Your Folders and files are visible ✔")
  elif(show_option is "n"):
    print("OK Bye Byes ❕")

if(hide_option is "y"):
  os.system("attrib +h /s /d")
  print("Your Folders and files are hidden ✔")
elif(hide_option is "n"):
  print("OK Bye Byes ❕")



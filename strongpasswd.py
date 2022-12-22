import random
import string

try:
  word_length = int(input('Password length: '))
except:
  print("ERROR, not a number")
else:
  components = [string.ascii_letters, string.digits]
  #components = [string.ascii_letters, string.digits, "!@#$%&"]
  chars = []
  for clist in components:
    for item in clist:
      chars.append(item)
  def generate_password():
    password = []
    for i in range(word_length):
      rchar = random.choice(chars)
      password.append(rchar)
    return "".join(password)
  print("Your password is:")
  print(generate_password())
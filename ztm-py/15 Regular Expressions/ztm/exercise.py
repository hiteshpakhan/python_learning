import re

password = "Luci@71421"

pass_pattern = re.compile(r"[A-Za-z0-9%$#@]{8,}\d")     #it will check 1> more than 8 characters 2> end with number 3>can also have symboals

check = pass_pattern.fullmatch(password)

print(check)
# output:-      <re.Match object; span=(0, 10), match='Luci@71421'>
import re

password = "Luci@714"

pass_pattern = re.compile(r"[A-Za-z0-9%$#@]{8,}\d")

check = pass_pattern.fullmatch(password)

print(check)
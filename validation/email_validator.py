import re 

def email_vali(email):
    pattern = r"[a-zA-Z0-9]{5,}[@]((gmail)|(yahoo)|(hotmail)|(outlook)|(bing))[.]((com)|(in)|(us)|(uk)|(eu))"
    return re.match(pattern,email) 

inp="bhavanajalla@gmail.com"

# if email_vali(inp) is not None:
#     print("valid")
# else:
#     print("not valid")

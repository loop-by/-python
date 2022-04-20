# Level 5: Extract the domain name from a URL
# https://www.codewars.com/kata/514a024011ea4fb54200004b
#
# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
#
# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

# What I did
def domain_name(url):
    head = url.find("www.")
    if head == -1:
        head = url.find("//")
        if head == -1:
            return url[0:url.find(".")]
        else:
            return url[head+2:url.find(".")]
    else:
        return url[head+4:url.find(".", head+4)]

# pythonic way
# def domain_name(url):
#     return url.split("//")[-1].split("www.")[-1].split(".")[0]

if domain_name("http://github.com/carbonfive/raygun") == "github":
    print("PASS")
if domain_name("http://www.zombie-bites.com") == "zombie-bites":
    print("PASS")
if domain_name("https://www.cnet.com") == "cnet":
    print("PASS")
if domain_name("www.xakep.ru") == "xakep":
    print("PASS")

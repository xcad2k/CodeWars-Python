import re


def domain_name(url):
    return re.sub("(.*//)|www.", "", url).split(".")[0]


print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))

import re


# pretty special use case... not working with subdomains (except www)
def domain_name(url):
    return re.sub("(https?://)?(www\.)?", "", url).split(".")[0]


print(domain_name("https://123.net"))

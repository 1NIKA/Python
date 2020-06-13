# --------სავარჯიშო 1--------
# import requests
# import csv
# from bs4 import BeautifulSoup
#
# url = "https://top.ge/"
# conn = requests.get(url)
# content = conn.text

# file = open("Top_Sites.csv", "w", encoding="utf-8_sig")
# writer = csv.writer(file)
# writer.writerow(["დასახელება", "ლინკი", "აღწერა", "ჰიტები(გუშინ)", "უნიკალური(გუშინ)"])
#
# soup = BeautifulSoup(content, "html.parser")
# tbody = soup.find("tbody")
# all_sites = tbody.find_all("tr")

# for i in all_sites:
#     title_bar = i.find("td", {"class": "tr_paddings", "style": "border-right: transparent !important;"})
#     title = title_bar.a.text.strip()
#     link = title_bar.a["href"]
#     description = i.find("td", {"class": "tr_paddings desc_pd hidden-xs ipad_hidden"}).text.strip()
#     hits = i.find("td", {"class": "tr_paddings number_fr hidden-xs text_center"}).span.text.strip()
#     unique = i.find("td", {"class": "tr_paddings number_fr text_center"}).span.text.strip()
#     print(title)
#     print(link)
#     print(description)
#     print(hits)
#     print(unique)
#     print("\n")
#     writer.writerow([title, link, description, hits, unique])
#
# file.close()

# --------სავარჯიშო 2--------
import requests
import csv
from bs4 import BeautifulSoup

file = open("books.csv", "w", encoding="utf-8_sig")
writer = csv.writer(file)
writer.writerow(["სათაური", "ავტორი", "ფასი", "ლინკი"])

num = 1
num_pages = 20
while num <= num_pages:
    url = f"http://lit.ge/index.php?page=books&send[shop.catalog][page]={num}"
    conn = requests.get(url)
    content = conn.text

    soup = BeautifulSoup(content, "html.parser")
    section = soup.find("section", {"class": "list-holder"})
    all_books = section.find_all("article")

    for each in all_books:
        title_bar = each.find("div", {"class": "title-bar"})
        title = title_bar.a.text.strip()
        link = title_bar.a["href"].strip()
        author = title_bar.b.a.text.strip()
        price = each.button.text.strip()
        writer.writerow([title, author, price, link])

    num += 1
    print(num)

file.close()

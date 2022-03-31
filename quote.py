import requests
import bs4
import colorama
from colorama import Fore, Back, Style

# add a fancy banner
print(Fore.RED + """
      
         ██████╗ ██╗   ██╗ ██████╗ ████████╗███████╗███████╗
        ██╔═══██╗██║   ██║██╔═══██╗╚══██╔══╝██╔════╝██╔════╝
        ██║   ██║██║   ██║██║   ██║   ██║   █████╗  ███████╗
        ██║▄▄ ██║██║   ██║██║   ██║   ██║   ██╔══╝  ╚════██║
        ╚██████╔╝╚██████╔╝╚██████╔╝   ██║   ███████╗███████║
         ╚══▀▀═╝  ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚══════╝
 ─────────────────────────────𝕾𝖍𝖆𝖗𝖆𝖉─────────────────────────────────     
                    """)
# ask for tag in yellow color
tag = input( Fore.YELLOW + "                [+] Please, Enter the tag name: " + Style.RESET_ALL)

# ask the user for the name of the file
filename = input( '\n' + Fore.YELLOW + "                [+] Enter the name of the file: " + Style.RESET_ALL)

# print collecting quotes in big blue text
print('\n' + Fore.WHITE + "  Starting...\n  Collecting quotes....." + Fore.WHITE)

# quotes from page 1 to page 10
source1 = "https://www.goodreads.com/quotes/tag/" + tag + "?page=1"
source2 = "https://www.goodreads.com/quotes/tag/" + tag + "?page=2"
source3 = "https://www.goodreads.com/quotes/tag/" + tag + "?page=3"
source4 = "https://www.goodreads.com/quotes/tag/" + tag + "?page=4"
source5 = "https://www.goodreads.com/quotes/tag/" + tag + "?page=5"


response = requests.get(source1 + source2 + source3 + source4 + source5)
# convert html to text
soup = bs4.BeautifulSoup(response.text, "html.parser")
# get the top quote
articles = soup.find_all("div", class_="quoteText")


# create a list of the top quote
article_list = []

for article in articles:
    article_list.append(article.text)
    # remove the newline character
    article_list[-1] = article_list[-1].replace("\n", "").strip().replace("   ", "") + '\n\n\n'
    # set number of quotes
    num_quotes = len(article_list)
    article_list[-1] = str(len(article_list)) + ". " + article_list[-1]
    
    article_list[-1] = Fore.BLUE + article_list[-1] + Style.RESET_ALL
    # set color for the duoble quotes
    article_list[-1] = article_list[-1].replace("“", Fore.GREEN + "“" + Style.RESET_ALL + Fore.YELLOW)




# put the quotes in the file
with open(filename, "w") as f:
    for article in article_list:
        f.write(article)

# calculate the total number of quotes in the file
with open(filename, "r") as f:
    total_quotes = len(f.readlines())

# finish the program with a message in blue
print('\n' + Fore.WHITE + "  Done! " + str(total_quotes) + " quotes have been saved in " + filename + "." + Style.RESET_ALL)

# ask the user if he wants to print the article_list
if input(Fore.GREEN + "  Do you want to read some of quote now? (Y/n): " + Style.RESET_ALL) == "n":
    print("Ok, bye!")
    
else:
    # read the file
    with open(filename, "r") as f:
        print(f.read())
    # remove spaces at the beginning and end of the quot article_list[-1] = article_list[-1].strip() remove double spaces article_list[-1] = article_list[-1].replace("  ", " ") every article in a new line article_list[-1] = article_list[-1] + "\n\n\n"

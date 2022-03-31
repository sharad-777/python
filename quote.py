# ------------ import modules ------------
import requests
import bs4
from rich.console import Console
from rich.progress import track
from time import sleep
console = Console()


# add a fancy banner
console.print( """
 \t  ██████╗ ██╗   ██╗ ██████╗ ████████╗███████╗███████╗
 \t ██╔═══██╗██║   ██║██╔═══██╗╚══██╔══╝██╔════╝██╔════╝
 \t ██║   ██║██║   ██║██║   ██║   ██║   █████╗  ███████╗
 \t ██║▄▄ ██║██║   ██║██║   ██║   ██║   ██╔══╝  ╚════██║
 \t ╚██████╔╝╚██████╔╝╚██████╔╝   ██║   ███████╗███████║
 \t  ╚══▀▀═╝  ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚══════╝
 ─────────────────────────────𝕾𝖍𝖆𝖗𝖆𝖉─────────────────────────────────   

                    """, style="red")


# ask for tag
# ask the user for the name of the file
# a fancy track progress
tag = input( "\t   [+] Please, Enter the tag name: ")
filename = input( "\t   [+] Enter the name of the file: ")+'\n'
console.print('\n\n\n' + "  Starting ......", style="blue")


def process_quotes():
        sleep(0.01)
for _ in track(range(100), description="[bold blue]  Collecting quotes"):
    process_quotes()



# --------------- sources for quotes ---------------
source1 = "https://www.goodreads.com/quotes/tag/" + tag + "?page=1"
source2 = "https://www.goodreads.com/quotes/tag/" + tag + "?page=2"
source3 = "https://www.goodreads.com/quotes/tag/" + tag + "?page=3"
source4 = "https://www.goodreads.com/quotes/tag/" + tag + "?page=4"
source5 = "https://www.goodreads.com/quotes/tag/" + tag + "?page=5"


# get response from sources
# set html parser
# get the quotes
response = requests.get(source1 + source2 + source3 + source4 + source5)
soup = bs4.BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("div", class_="quoteText")


# create a list of the quotes
# remove newline characters from the quotes
# remove triple spaces from the quotes
# put every quote in a newl line
# add number of the quote to the beginning of the quote
# print the quotes
quotes = []
for i in range(len(articles)):
    quotes.append(articles[i].text.replace('\n', '').replace('   ', '')+ '\n')
    quotes[i] = str(i+1) + '. ' + quotes[i]
    # console.print(quotes[i], style="yellow")



# write the quotes to the file
# calculate the number of quotes in the file
# print the number of quotes
with open(filename + '.txt', 'w') as file:
    for quote in quotes:
        file.write(quote)

with open(filename + '.txt', 'r') as file:
    quotes_number = len(file.readlines())


    console.print('\n' + "  Done!\n  " + str(quotes_number) + " quotes collected and saved in "+ filename , style="bold green")


# ask the user if he want to read some quotes
# if yes, print the quotes in yellow color
# if no, exit the program
if input ("\n  Do you want to read some quotes? (Y/n): ") == 'n':
   console.print('\n' + "  OK! Bye!", style="bold red")
else:
    console.print('\n' "\t\t\t Reading quotes.....", style="bold blue" + '\n\n')
    with open(filename + '.txt', 'r') as file:
        for i in range(quotes_number):
            console.print(file.readline(), style="yellow")
    console.print('\n' + "[white]  Done!\n  " + str(quotes_number) + " quotes readed!", style="bold white")


import    pyfiglet
def print_ascii_art(text,font="stright"):
    try:
        ascii_art =pyfiglet.figlet_format(text,font=font)
        print(ascii_art)
    exceot:
        print(f"\n{text}\n")
print_ascii_art("Grey Hat  Thamizha", font="big")

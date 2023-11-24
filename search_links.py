# Display a message before running the script
print("                  Subu")
print("                    .")
print("                    .")
print("                    .")
print("         ░█▀▀░█░█░█░█░█▀█░█▀█░█░█")
print("         ░▀▀█░█░█░█░█░█░█░█▀█░█▀▄")
print("         ░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀")
print("                    .")
print("                    .")
print("                    .")
print("                  Rownak")


def generate_google_search_links(names):
    search_links = []
    for name in names:
        query = f"https://www.google.com/search?q={'+'.join(name.split())}"
        search_links.append(query)
    return search_links

# Read Input names from the input text file
with open("input_names.txt", "r") as file:
    names_input = file.read()

# Process the input to create a list of names
name_list = [name.strip() for name in names_input.split("\n") if name.strip()]

# Generate and print Google search links
search_links = generate_google_search_links(name_list)
for name, link in zip(name_list, search_links):
    print(f"Name: {name}")
    print(f"Google Search Link: {link}")
    print("=" * 20)


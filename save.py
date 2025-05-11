import json
import subprocess

LINKS_FILE = "links.json"

def load_links():
    try:
        with open(LINKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_links(links):
    with open(LINKS_FILE, "w") as file:
        json.dump(links, file, indent=4)

def add_link(new_link):
    links = load_links()
    links.append(new_link)
    save_links(links)

def push_to_github():
    subprocess.run(["git", "add", LINKS_FILE])
    subprocess.run(["git", "commit", "-m", "Updated links"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    new_link = input("Enter a new link: ")
    add_link(new_link)
    push_to_github()
    print("Link added and pushed to GitHub!")

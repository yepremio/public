
markdown_path = "content/index.md"
markdown = get_markdown(markdown_path)


def get_markdown(path):
    with open(path) as f:
        return f.read()




def extract_title(markdown):
    

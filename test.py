import markdown

#converts input string into HTML-style string

def convert(text):
    html = markdown.markdown(text)
    print html

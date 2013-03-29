import markdown

#imported markdown (version 2.3.1) package, which converts string to HTML string
 
#converts input text into HTML-style string
def convert(text):
    html = markdown.markdown(text)
    print html

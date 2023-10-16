from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_h1():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


def find_list_items():
    li_tags = simple_soup.find_all('li')
    # removing the tags
    li_items = [name.string for name in li_tags]
    print(li_items)


def find_subtitle():
    p_tag = simple_soup.find('p', {'class': 'subtitle'})
    content = p_tag.string
    print(content)


# get returns None instead of KeyError if key doesn't exist
# get('class',[]) means instead of None it's gonna return [] if key doesn't exist
def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    print(paragraphs)
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraph[0])


find_h1()
find_list_items()
find_subtitle()
find_other_paragraph()

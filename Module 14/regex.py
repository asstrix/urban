import re

sample_html = """<img src='https://example.com/image1.jpg'> 
<img src='http://example.com/image2.png'> <img src='https://example.com/image3.gif'>"""


def extract_image_links(html_text):
    res = re.findall(r'["\'](.*?\.(?:jpg|jpeg|png|gif))["\']', html_text)
    return res


image_links = extract_image_links(sample_html)
if image_links:
    for image_link in image_links:
        print(image_link)
else:
    print("Нет ссылок с картинками в HTML тексте.")
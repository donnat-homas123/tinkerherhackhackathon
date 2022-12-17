from linkpreview import Link, LinkPreview, LinkGrabber

url = "http://github.com"
grabber = LinkGrabber(
    initial_timeout=20,
    maxsize=1048576,
    receive_timeout=10,
    chunk_size=1024,
)
content, url = grabber.get_content(url)
link = Link(url, content)
preview = LinkPreview(link, parser="lxml")
print("title:", preview.title)
print("description:", preview.description)
print("image:", preview.image)
print("force_title:", preview.force_title)
print("absolute_image:", preview.absolute_image)
print("site_name:", preview.site_name)
import requests
try:
    r = requests.head("http://github.com")
    print(r.status_code)
    print("success")
    # prints the int of the status code. Find more at httpstatusrappers.com :)
except requests.ConnectionError:
    print("failed to connect")
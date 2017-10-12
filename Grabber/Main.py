
import mechanize
import cookielib
import re

def get_webpage(url):

    # Set up a Mechanize Browser and load up the cookiejar
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Sets our browser to handle refreshing.
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    # sets our Browser to immitate a browser
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    #Set some flags for operation type
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    try:
        r = br.open(url)
        htmltextz = r.read()

    except:
        print url
        htmltextz = '0'

    return htmltextz
def get_target_data( style, html):
    finder = re.compile(style)
    pics = re.findall(finder, html)
    return pics

# Get webpage html
url = "https://www.google.com/search?q=bulbasaur&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjA_a7f9-nWAhWERiYKHZPsCP8Q_AUICigB&biw=1200&bih=887"
text = get_webpage(url)

# find the pictures in the html
pic_style = '<img[^.]*src="(.+?)"'
#pic_style = '<link href="(.+?)" rel'

pics_url = get_target_data(pic_style, text)

print text
for pic in pics_url:
    print pic

#print pics_url
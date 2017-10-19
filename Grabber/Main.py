import mechanize
import cookielib
import re
import time


# Search Image Format
# https://www.google.com/search?tbm=isch&source=hp&biw=1920&bih=964&q=squirtle&oq=squirtle&gs_l=img.3..35i39k1j0l9.5053.6878.0.7036.13.13.0.0.0.0.290.1551.0j6j2.8.0....0...1.1.64.img..5.8.1548.0...0.c9St6yDJ1k8#imgrc=_

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

''' Open File '''
# Open File to store Pictures List
currenTime = time.strftime("_%d.%m.%Y_%H.%M.%S")
write_text_page_name = "Picture_Urls/PicsList" + currenTime + ".txt"
write_text_page = open(write_text_page_name,"w")

## find the pictures in the html
pic_style = '<img[^.]*src="(.+?)"'

# Get webpage html
# Charmander
# url = "https://www.google.com/search?q=squirtle&source=lnms&tbm=isch&sa=X&ved=0ahUKEwipr5n2gerWAhXMbhQKHRidD2gQ_AUICigB&biw=1920&bih=963"
# Bulbasor

url_example = "https://www.google.com/search?tbm=isch&source=hp&biw=1920&bih=964&q=squirtle&oq=squirtle&gs_l=img.3..35i39k1j0l9.5053.6878.0.7036.13.13.0.0.0.0.290.1551.0j6j2.8.0....0...1.1.64.img..5.8.1548.0...0.c9St6yDJ1k8#imgrc=_"
url_base = "https://www.google.com/search?tbm=isch&source=hp&biw=1920&bih=964&q="
url_mid = "&oq"
url_end = "&gs_l=img.3..35i39k1j0l9.5053.6878.0.7036.13.13.0.0.0.0.290.1551.0j6j2.8.0....0...1.1.64.img..5.8.1548.0...0.c9St6yDJ1k8#imgrc=_"
# url_mid = "squirtle&oq=squirtle"
# url = "https://www.google.com/search?q=bulbasaur&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjA_a7f9-nWAhWERiYKHZPsCP8Q_AUICigB&biw=1200&bih=887"


read_text_page_name = "Pokenames.txt"
read_text_page = open(read_text_page_name,"r")



## Grab Pokemon Names
names_list = []
types_list = [
    'Ghost',
    'Fighting',
    'Psychic',
    'Steel',
    'Fairy',
    'Dark',
    'Dragon',
    'Dark',
    'Grass',
    'Flying',
    'Electric',
    'Fire',
    'Bug',
    'Poison',
    'Rock',
    'Water',
    'Ground',
    'Ice',
    'Normal',
    'forme',
    'black',
    'white',
    'mega',
    'style'
    ]
for line in read_text_page:
    #print line
    try :
        a = int(line)
    except :
        if (line[0:-1] not in types_list):
            names_list.append(line.lower())

read_text_page.close()

## Construct Webpage Url
## Visist Web Page
## Grab Links Returned on all Webpages

for name in names_list:
    url = url_base + str(name) #+ url_mid + str(name) + url_end
    try :
        print "Grabbing data for " + name
        write_text_page.write(name)
        web_return = get_webpage(url)
        pics_url = get_target_data(pic_style, web_return)
        for link in pics_url:
            write_text_page.write(link)
            write_text_page.write("\n")
    except :
        print "Was not able to get data for : " + name

write_text_page.close()

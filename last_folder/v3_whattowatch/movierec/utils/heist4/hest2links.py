import guidebox
import json

guidebox.api_key = 'd3c0fd429d3d77cce364497b2b4d5fc3f8d5c0f9'
guidebox.Region = 'US'


def getNetflixLinks():
    identifiers = []
    i = 0
    with open("netflix_idlist.txt", "r") as file:
        for line in file:
            identifiers.append(int(line))

    fo = open("netflix_links.txt", "a")

    for iden in identifiers:
        i += 1
        movie_detail = guidebox.Movie.retrieve(id=iden)
        detail = json.loads(movie_detail.__str__())

        netflix_link = ''

        for each in detail['subscription_web_sources']:
            if each['source'] == 'netflix':
                netflix_link = each['link']

        fo.write(str(iden) + " " + str(netflix_link) + "\n")
        print "Got link for " + detail['title'] + ", Movie#: " + str(i)
    fo.close()
    print "Done"
    print guidebox.Quota.retrieve()


def getHuluLinks():
    identifiers = []
    i = 0
    with open("hulu_idlist.txt", "r") as file:
        for line in file:
            identifiers.append(int(line))

    fo = open("hulu_links.txt", "a")

    for iden in identifiers:
        i += 1
        movie_detail = guidebox.Movie.retrieve(id=iden)
        detail = json.loads(movie_detail.__str__())

        hulu_link = ''

        for each in detail['subscription_web_sources']:
            if each['source'] == 'hulu_plus':
                hulu_link = each['link']

        fo.write(str(iden) + " " + str(hulu_link) + "\n")
        print "Got link for " + detail['title'] + ", Movie#: " + str(i)
    fo.close()
    print "Done"
    print guidebox.Quota.retrieve()


def getHBOLinks():
    identifiers = []
    i = 0
    with open("hbo_idlist.txt", "r") as file:
        for line in file:
            identifiers.append(int(line))

    fo = open("hbo_links.txt", "a")

    for iden in identifiers:
        i += 1
        movie_detail = guidebox.Movie.retrieve(id=iden)
        detail = json.loads(movie_detail.__str__())

        hbo_link = ''

        for each in detail['subscription_web_sources']:
            if each['source'] == 'hbo_now':
                hbo_link = each['link']

        fo.write(str(iden) + " " + str(hbo_link) + "\n")
        print "Got link for " + detail['title'] + ", Movie#: " + str(i)
    fo.close()
    print "Done"
    print guidebox.Quota.retrieve()


#getHBOLinks()
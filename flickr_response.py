import json


class Photo(object):

    def __init__(self, photo_diction):
        self.owner = {
            "username": photo_diction["owner"]["username"],
            "realname": photo_diction["owner"]["realname"],
            "location": photo_diction["owner"]["location"]
        }
        self.title = photo_diction["title"]["_content"]
        self.tags = []
        for tag in photo_diction["tags"]["tag"]:
            self.tag.append(tag["raw"])
        self.dates = photo_diction["dates"]["taken"]
        self.id = photo_diction["id"]
        self.url = photo_diction["urls"]["url"][0]["_content"]
        self.license = photo_diction["license"]

    def __str__(self):
        return self.title

    def __repr__(self):
        return "ID: {0}, Title: {1}, URL: {2}".format(
            self.id, self.title, self.url)

    def __contains__(self, test_string):
        return (test_string in self.tags or test_string in self.title)


#open(filename, mode)
with open("sample_diction.json", "r") as f:
    f_string = f.read()
    response_diction = jason.loads(f_string)

pd = response_diction["photo"]
photo = Photo(pd)

print(photo)
print(repr(photo))

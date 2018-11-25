class Member:
    def __init__(self, id, name, title, description):
        self.id = id
        self.name = name
        self.title = title
        self.description = description


class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username


members = [Member(1,
                  "Viktor Eriksson den första den andre",
                  "Vice vice",
                  "Kodapa från Bryssel"),
           Member(2,
                  "Carl-Johan Backman",
                  "World Leader",
                  "Carl-Johan might seem like the perfect"
                  " human being. But behind the facade filled with charities"
                  " and puppies a man with a dark, german, side appears."),
           Member(3,
                  "Gman Gmanovic",
                  "Bredus Bandus Fixus",
                  "G Dizzle, my Nizzle."),
           Member(4,
                  "Mr T",
                  "Ekerös Göran Kropp",
                  "A man with the perfect beard, a well functioning brain"
                  " and an interest for boring stuff like hiking and"
                  " Fjällräven-pants is hard to find."
                  " But Riksdawgen did it!")]

users = [User(1, "Vieriksson")]

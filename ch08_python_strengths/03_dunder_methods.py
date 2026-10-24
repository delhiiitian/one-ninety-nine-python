"""8.3 Special (dunder) methods: making objects feel built in.

Real-world comparison: universal plugs. If your appliance has the
standard plug, it works in every socket. If your class has the
standard methods (__str__, __add__, __len__ ...), it works with
print(), +, len() and friends.
"""


class Money:
    def __init__(self, rupees):
        self.rupees = rupees

    def __str__(self):                 # used by print()
        return f"Rs {self.rupees:,}"

    def __repr__(self):                # used in lists and the shell
        return f"Money({self.rupees})"

    def __add__(self, other):          # used by +
        return Money(self.rupees + other.rupees)

    def __eq__(self, other):           # used by ==
        return self.rupees == other.rupees

    def __lt__(self, other):           # used by < and sorted()
        return self.rupees < other.rupees


class Playlist:
    def __init__(self, songs):
        self.songs = list(songs)

    def __len__(self):                 # used by len()
        return len(self.songs)

    def __getitem__(self, index):      # used by [ ] and for loops
        return self.songs[index]

    def __contains__(self, song):      # used by in
        return song in self.songs


rent = Money(25000)
food = Money(8000)
print("Total:", rent + food)
print("Equal?", Money(5) == Money(5))
print("Sorted:", sorted([rent, food, Money(1200)]))

mix = Playlist(["Song A", "Song B", "Song C"])
print("Songs:", len(mix), "| First:", mix[0], "| Has Song B?", "Song B" in mix)
for song in mix:
    print("Playing", song)

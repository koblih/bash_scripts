
#create precious stone
#no more than 5 precious stones can be held at one given time
#delete first stone if sixth one is created

class PresciousStones:
    stone_list = []
    def create_precious_stone(self, name):
        self.name = name
        self.update_stone_list()

    def update_stone_list(self):
        self.stone_list.append(self.name)
        if len(self.stone_list) > 5:
            self.stone_list.pop(0)
        print(self.stone_list)


pocket = PresciousStones()
pocket.create_precious_stone('diamond')
pocket.create_precious_stone('ruby')
pocket.create_precious_stone('krystal')
pocket.create_precious_stone('emerald')
pocket.create_precious_stone('coal')
pocket.create_precious_stone('amethyst')

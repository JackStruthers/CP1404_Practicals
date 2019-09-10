class Plant:

    def __init__(self, name="", height=0.0, growth_rate=0.0):
        self.name = name
        self.height = height
        self.growth_rate = growth_rate

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.height, self.growth_rate)

    def water(self, water):
        self.height += water * self.growth_rate

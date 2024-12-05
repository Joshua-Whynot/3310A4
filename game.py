#game datastructure, filled in by file
#ID,Name,Average User Rating,User Rating Count,Developer,Size
class Game:
    def __init__(self, ID, name, avgUserRating, userRatingCount, developer, size):
        self.ID = ID
        self.name = name
        self.avgUserRating = avgUserRating
        self.userRatingCount = userRatingCount
        self.developer = developer
        self.size = size
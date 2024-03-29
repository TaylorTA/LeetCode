class LUPrefix:

    def __init__(self, n: int):
        self.videos = [False] * n
        self.best = 0
        

    def upload(self, video: int) -> None:
        self.videos[video-1] = True
        while self.videos[self.best]:
            self.best += 1
            if self.best >= len(self.videos):
                break

    def longest(self) -> int:
        return self.best


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()

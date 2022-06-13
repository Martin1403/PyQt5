
class STATS(dict):
    def __init__(self) -> None:
        super().__init__()
        self.update(
            cpu=dict(),
            gpu=dict(),
            memo=dict(),
        )

    def __str__(self):
        return f'💻 {self.__class__.__name__}: {[f"{i}={self.get(i)}" for i in self.keys()]})'

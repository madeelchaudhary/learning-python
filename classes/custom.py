class Tags:
    def __init__(self) -> None:
        self.__tags = {}

    def add(self, tag: str):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag: str):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag: str, count: int):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


tags = Tags()
tags.add("Python")
tags.add("Python")
tags.add("python")

print(tags["python"])
tags["python"] = 10
print(tags["python"])
print(len(tags))

print(tags._Tags__tags)

from .base import Base


class PreCommit(Base):

    def to_dict(self):
        data = super().to_dict()
        print(data)
        for ext in getattr(data, self.KEY_COMMANDS, {}).keys():
            print(ext)
            data[ext].append('git add')
        # print(data)
        return data

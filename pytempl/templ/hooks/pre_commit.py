from .base import Base


class PreCommit(Base):

    def to_dict(self):
        data = super().to_dict()
        for ext in getattr(data, self.KEY_COMMANDS, {}).keys():
            data[ext].append('git add')
        # print(data)
        return data

from hanalmot.utils import load_hanalmot

hanalmot = load_hanalmot()


class HanalmotToken(object):
    def __init__(self, letter, pos):
        self.letter = letter
        self.pos = pos

    @staticmethod
    def from_java(java_token):
        return HanalmotToken(java_token.letter, java_token.pos)

    def __repr__(self):
        return '({},{})'.format(self.letter, self.pos)


def tokenize(text):
    tokenized = hanalmot.tokenize(text)
    return tuple(HanalmotToken.from_java(t) for t in tokenized)


if __name__ == '__main__':
    print(tokenize('집에 가서 잠을 자고 싶은 마음 뿐이다.'))



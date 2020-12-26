class DiagonalParser:
    def __init__(self, p: "PathParser"):
        self._p = p
        self._v = None

    def set_ns(self, ns: str):
        self._v = ns

    def __call__(self, v: str):
        self._p.parse = self._p.default_parser
        self._p.parse(self._v + v)


class DefaultParser:
    def __init__(self, p: "PathParser"):
        self._p = p

    def __call__(self, v: str):
        if v == "n" or v == "s":
            self._p.parse = self._p.diagonal_parser
            self._p.diagonal_parser.set_ns(v)
        else:
            self._p.path.append(v)


class PathParser:
    def __init__(self):
        self.path = []
        self.default_parser = DefaultParser(self)
        self.diagonal_parser = DiagonalParser(self)
        self.parse = self.default_parser

    def _add(self, v):
        self.parse(v)

    def __call__(self, p):
        self.path = []
        for c in p:
            self._add(c)
        return self.path


path_parser = PathParser()

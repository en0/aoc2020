from abc import ABC, abstractmethod
from typing import ContextManager, IO, Generator
from contextlib import contextmanager
from os.path import join as join_path


class SolutionABC(ABC):

    def __init__(self, resource_path: str, testing: bool = False, *args, **kwargs):
        self.testing = testing
        self.resource_path = resource_path

    def get_resource_name(self, name: str) -> str:
        return f"test-{name}" if self.testing else name

    @contextmanager
    def load_resource(self, name: str, mode: str = 'r') -> ContextManager[IO]:
        path = join_path(self.resource_path, self.get_resource_name(name))
        try:
            fd = open(path, mode)
            yield fd
        finally:
            fd.close()

    def resource_lines(self, name: str, xfrm=None) -> Generator:
        xfrm = xfrm or (lambda x: x)
        with self.load_resource(name, 'r') as fd:
            for line in fd:
                yield xfrm(line.rstrip('\n'))

    @classmethod
    def read_until(cls, fp, predicate=None, xfrm=None):
        predicate = predicate or (lambda s: False)
        xfrm = xfrm or (lambda x: x)
        for line in fp:
            ln = line.rstrip("\n")
            if predicate(ln):
                break
            yield xfrm(ln)

    def check(self):
        return self.expected == self.solve()

    @abstractmethod
    def solve(self) -> any:
        raise NotImplementedError()

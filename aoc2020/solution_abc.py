from abc import ABC, abstractmethod
from contextlib import contextmanager
from os.path import join as join_path


class SolutionABC(ABC):

    def __init__(self, resource_path: str, testing: bool = False):
        self.testing = testing
        self.resource_path = resource_path

    @contextmanager
    def load_resource(self, name: str, mode: str = 'r'):
        resource_name = f"test-{name}" if self.testing else name
        path = join_path(self.resource_path, resource_name)
        try:
            fd = open(path, mode)
            yield fd
        finally:
            fd.close()

    def resource_lines(self, name: str, xfrm=None):
        xfrm = xfrm or (lambda x: x)
        with self.load_resource(name, 'r') as fd:
            for line in fd:
                yield xfrm(line.rstrip('\n'))

    def check(self):
        return self.expected == self.solve()

    @abstractmethod
    def solve(self) -> any:
        raise NotImplementedError()

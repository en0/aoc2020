from argparse import ArgumentParser
from time import perf_counter
from importlib import import_module
from os.path import dirname, basename, join as join_path
from .errors import NoSolutionError
from .solution_abc import SolutionABC


def get_opts():
    ap = ArgumentParser()
    ap.add_argument("--test", action="store_true", default=False, help="Runs using test input.")
    ap.add_argument("--check", action="store_true", default=False, help="Runs using test input and checks result with "
                                                                        "expected.")
    ap.add_argument("DAY", choices=[str(i) for i in range(1, 26)], help="The Day")
    ap.add_argument("PART", choices=['1', '2'], help="The Part")
    return ap.parse_args()


def build_solution(day, part, testing=False) -> SolutionABC:
    module = import_module(f".day_{day.zfill(2)}.part_{part}", "aoc2020")
    module_path = dirname(module.__file__)
    solution = getattr(module, "Solution")
    return solution(join_path(module_path, "resources"), testing)


def main():
    opts = get_opts()
    solution = build_solution(opts.DAY, opts.PART, opts.test or opts.check)

    def show(result, detail=None):
        print(f"AoC[2020.{opts.DAY}.{opts.PART}] -> {result}")
        if detail:
            print(f"[+], {detail}")

    def run_check():
        try:
            success = solution.check()
            show("PASS" if success else "FAILED")
            if not success:
                exit(1)
        except Exception as ex:
            show("FAILED", str(ex))
            exit(2)

    def run_solve():
        try:
            show(solution.solve())
        except NoSolutionError:
            show("Unable to find a solution.")
            exit(1)

    perf_counter()
    if opts.check:
        run_check()
    else:
        run_solve()
    print(f"[+] Perf: {perf_counter()}")


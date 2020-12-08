import re
from typing import Tuple, List

re_rule = re.compile(r"^(\w*\ \w*)\ bags?\ contain\ (.*)\.$")
re_content = re.compile(r"^(\d*)\ (\w*\ \w*)\ bags?")


def parse_rule(rule: str) -> Tuple[str, List[Tuple[str, int]]]:
    rule_match = re_rule.fullmatch(rule)
    if not rule_match:
        raise ValueError("Rule does not conform.")
    bag_content = []
    bag_name, content_str = rule_match.groups()
    for content in content_str.split(","):
        content_match = re_content.fullmatch(content.strip(" "))
        if not content_match:
            continue
        content_count, content_name = content_match.groups()
        bag_content.append((content_name, int(content_count)))
    return bag_name, bag_content

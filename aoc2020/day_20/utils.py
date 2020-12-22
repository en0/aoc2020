def rotate_matrix(matrix):
    return matrix


def cache(fn):
    _cache = {}
    def _wrap(tile):
        k, m = tile
        key = f"{k}:{m}"
        if key not in _cache:
            _cache[key] = fn(tile)
        return _cache[key]
    return _wrap

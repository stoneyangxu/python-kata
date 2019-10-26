def reverse(S, start, end):
    print(f"reverse(S, {start}, {end})")
    if start >= end:
        return
    S[start], S[end - 1] = S[end - 1], S[start]
    reverse(S, start + 1, end - 1)


if __name__ == '__main__':
    S = [4, 3, 6, 2, 6]
    reverse(S, 0, len(S))
    print(S)

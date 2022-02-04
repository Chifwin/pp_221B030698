x, y = map(int, input().split())
print("\n".join(" ".join(list(map(str, i))) for i in (sorted([list(map(int, input().split())) for _ in range(int(input()))], key = (lambda p:(p[0]-x)**2 + (p[1]-y)**2)))))

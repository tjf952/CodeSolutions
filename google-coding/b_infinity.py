import math

def solve():
	r,a,b = map(int, input().split())
	compute = [lambda rad: rad*a, lambda rad: math.floor(rad/b)]
	total, idx = 0, 0
	while r > 0:
		total += r**2
		r = compute[idx](r)
		idx ^= 1
	return total*math.pi

def main():
	cases = int(input())
	for i in range(cases):
		answer = solve()
		print(f"Case #{i+1}: {answer}")

if __name__ == "__main__":
	main()
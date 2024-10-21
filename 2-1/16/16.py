import sys
import math

INF = float('inf')


def main():
    # Redirect input and output
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        n = int(infile.readline().strip()) + 1

        # Read adjacency matrix
        a = [[0] * n for _ in range(n)]
        for i in range(1, n):
            a[i][1:n] = list(map(int, infile.readline().strip().split()))

        # Initialize DP table
        dp = [[INF] * (1 << n) for _ in range(n)]
        dp[0][0] = 0

        # Fill DP table
        for mask in range(1 << n):
            for i in range(n):
                for j in range(n):
                    if (mask & (1 << j)) > 0:
                        dp[i][mask] = min(dp[i][mask], dp[j][mask ^ (1 << j)] + a[i][j])

        # Write the result to the output file
        outfile.write(str(dp[0][(1 << n) - 1]) + '\n')

        # Find the path
        i = 0
        mask = (1 << n) - 1
        path = []

        while mask > 0:
            for j in range(n):
                if (mask & (1 << j)) > 0 and dp[i][mask] == dp[j][mask ^ (1 << j)] + a[i][j]:
                    if j != 0:
                        path.append(j)
                    i = j
                    mask ^= (1 << j)
                    break
        path.reverse()  # Reverse to get the path from start to finish

        # Write the path to the output file
        outfile.write(' '.join(map(str, path)) + '\n')


if __name__ == '__main__':
    main()

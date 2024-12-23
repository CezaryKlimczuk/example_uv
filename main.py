from plot_path import plot_path
from random_walk import generate_random_walk


def main():
    print("Hello from example-uv!")
    print("Generating random walk...")

    walk = generate_random_walk(10000)
    print("Plotting walk...")

    plot_path(walk)


if __name__ == "__main__":
    main()

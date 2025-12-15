from runner import TSPRunner

if __name__ == "__main__":
    runner = TSPRunner()
    path, cost = runner.run(max_steps=50)

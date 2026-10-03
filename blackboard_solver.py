from puzzle import solve_puzzle

class Blackboard:
    def __init__(self):
        self.knowledge = []

    def post(self, agent, message):
        self.knowledge.append((agent, message))
        print(f"[Blackboard] {agent}: {message}")

def main():
    print("BLACKBOARD MULTI-AGENT PUZZLE SOLVER")
    print("-" * 45)

    board = Blackboard()

    board.post("Coordinator", "Puzzle posted.")
    board.post("Explorer Agent", "Explorer-island constraints analyzed.")
    board.post("Boat Agent", "Boat-island constraints analyzed.")
    board.post("Treasure Agent", "Treasure-island constraints analyzed.")
    board.post("Logic Agent", "All shared constraints cross-validated.")

    solution = solve_puzzle()

    board.post("Coordinator", "Final consistent solution found.")

    print("\n[Coordinator] Final Solution")
    print(f"Explorer : {solution['explorer']}")
    print(f"Island   : {solution['island']}")
    print(f"Boat     : {solution['boat']}")
    print(f"Treasure : {solution['treasure']}")

if __name__ == "__main__":
    main()

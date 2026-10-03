from puzzle import solve_puzzle

def main():
    print("CENTRALIZED MULTI-AGENT PUZZLE SOLVER")
    print("-" * 45)
    print("Master Agent -> Worker Agents -> Master Agent")
    solution = solve_puzzle()

    print("\n[Master] Final Solution")
    print(f"Explorer : {solution['explorer']}")
    print(f"Island   : {solution['island']}")
    print(f"Boat     : {solution['boat']}")
    print(f"Treasure : {solution['treasure']}")

if __name__ == "__main__":
    main()

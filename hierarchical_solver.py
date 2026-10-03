from puzzle import solve_puzzle

def main():
    print("HIERARCHICAL MULTI-AGENT PUZZLE SOLVER")
    print("-" * 45)
    print("Main Coordinator")
    print("  ├── Island Coordinator")
    print("  └── Resource Coordinator")

    solution = solve_puzzle()

    print("\n[Main Coordinator] Final Solution")
    print(f"Explorer : {solution['explorer']}")
    print(f"Island   : {solution['island']}")
    print(f"Boat     : {solution['boat']}")
    print(f"Treasure : {solution['treasure']}")

if __name__ == "__main__":
    main()

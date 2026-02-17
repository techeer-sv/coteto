from collections import deque


def solution(cards1, cards2, goal):

    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    while goal:
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
            goal.popleft()
        else:
            return "No"
    return "Yes"


def main():
    inputs = [
        {
            "cards1": ["i", "drink", "water"],
            "cards2": ["want", "to"],
            "goal": ["i", "want", "to", "drink", "water"],
            "result": "Yes",
        },
        {
            "cards1": ["i", "water", "drink"],
            "cards2": ["want", "to"],
            "goal": ["i", "want", "to", "drink", "water"],
            "result": "No",
        },
    ]

    for i, tc in enumerate(inputs):
        result = solution(tc["cards1"], tc["cards2"], tc["goal"])
        assert (
            result == tc["result"]
        ), f"[{i}] 실패: expected={tc['result']} output={result}"
        print(f"[{i}] 통과")


if __name__ == "__main__":
    main()

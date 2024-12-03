import random
import datetime

def craft_code_snippet():
    code_snippets = [
        "def merge_sort(arr):\n    if len(arr) > 1:\n        mid = len(arr)//2\n        left_half = arr[:mid]\n        right_half = arr[mid:]\n        merge_sort(left_half)\n        merge_sort(right_half)\n        i = j = k = 0\n        while i < len(left_half) and j < len(right_half):\n            if left_half[i] < right_half[j]:\n                arr[k] = left_half[i]\n                i += 1\n            else:\n                arr[k] = right_half[j]\n                j += 1\n            k += 1\n        while i < len(left_half):\n            arr[k] = left_half[i]\n            i += 1\n            k += 1\n        while j < len(right_half):\n            arr[k] = right_half[j]\n            j += 1\n            k += 1",
        "class Strategy:\n    def execute(self):\n        pass\n\nclass ConcreteStrategyA(Strategy):\n    def execute(self):\n        print('Strategy A executed')\n\nclass ConcreteStrategyB(Strategy):\n    def execute(self):\n        print('Strategy B executed')",
        "def exponential_backoff(retries):\n    import time\n    delay = 1\n    for attempt in range(retries):\n        time.sleep(delay)\n        delay *= 2"
    ]
    chosen_code = random.choice(code_snippets)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"# Crafted on {timestamp}\n\n{chosen_code}"

if __name__ == "__main__":
    with open("crafted_code.py", "w") as file:
        file.write(craft_code_snippet())

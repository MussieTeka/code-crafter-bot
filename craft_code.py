import random
import datetime

def craft_code_snippet():
    code_snippets = [
        "def merge_sort(arr): if len(arr) > 1: mid = len(arr)//2; left_half = arr[:mid]; right_half = arr[mid:]; merge_sort(left_half); merge_sort(right_half); i = j = k = 0; while i < len(left_half) and j < len(right_half): if left_half[i] < right_half[j]: arr[k] = left_half[i]; i += 1 else: arr[k] = right_half[j]; j += 1; k += 1; while i < len(left_half): arr[k] = left_half[i]; i += 1; k += 1; while j < len(right_half): arr[k] = right_half[j]; j += 1; k += 1",
        "class Strategy: def execute(self): pass\nclass ConcreteStrategyA(Strategy): def execute(self): print('Strategy A executed')\nclass ConcreteStrategyB(Strategy): def execute(self): print('Strategy B executed')",
        "def exponential_backoff(retries): import time; delay = 1; for attempt in range(retries): time.sleep(delay); delay *= 2"
    ]
    chosen_code = random.choice(code_snippets)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f\"\"\"# Crafted on {timestamp}\n\n{chosen_code}\"\"\"

if __name__ == "__main__":
    with open("crafted_code.py", "w") as file:
        file.write(craft_code_snippet())

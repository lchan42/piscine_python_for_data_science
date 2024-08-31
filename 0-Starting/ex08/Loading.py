# def ft_tqdm(lst: range) -> None:
# #your code here
from time import sleep


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i, elem in enumerate(lst):
        progress = i + 1
        percentage = (progress / total) * 100
        bar_length = int(percentage // 2)
        bar = f"[{'=' * bar_length}>{' ' * (50 - bar_length)}]"
        time_left = (total - progress) * 0.005

        yield f"{percentage:.1f}%|{bar}| {progress}/{total} [{time_left:.2f}s per iteration]"


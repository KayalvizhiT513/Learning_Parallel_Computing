import multiprocessing as mp

print(f"Number of cpu: {mp.cpu_count()}")

# Output: Number of cpu: 8
# 4 physical cores with 2 logical cores each, thus 8 cores

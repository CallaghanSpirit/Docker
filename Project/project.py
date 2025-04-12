import time
import numpy as np
from tqdm import tqdm

total = 1000
item_tqdm = tqdm(range(total))

for i in item_tqdm:
    res = i/100
    # print(f"sin({res}) = {np.sin(res):.4f}")
    item_tqdm.set_description(f"sin({res}) = {np.sin(res):.4f}" )
    time.sleep(1)
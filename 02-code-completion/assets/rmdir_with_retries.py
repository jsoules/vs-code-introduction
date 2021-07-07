import os
import shutil
import time

def rmdir_with_retries(dirname: str, num_retries: int, delay_between_tries: float=1):
    for retry_num in range(1, num_retries + 1):
        if not os.path.exists(dirname):
            return
        try:
            shutil.rmtree(dirname)
            break
        except: # pragma: no cover
            if retry_num < num_retries:
                print(f'Retrying to remove directory: {dirname}')
                time.sleep(delay_between_tries)
            else:
                raise Exception(
                    f'Unable to remove directory after {num_retries} tries: {dirname}'
                )
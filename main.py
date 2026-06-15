import os
import platform

def get_platform_release_info():
    res = "N/A"
    try:
        res = os.popen('cat /etc/os-release | grep "^PRETTY_NAME"').read().strip().split("=")[1].strip('"'),
    except Exception as e:
        pass
    return res

def get_platform_runtime_info():
    return {
        "python_version": os.popen("python --version").read().strip(),
        "os": os.uname().sysname,
        "architecture": os.uname().machine,
        "kernel release": platform.release(),
        "full system info": platform.platform(),
        "platform release": get_platform_release_info(),
        #there is no platform.freedesktop_os_release() in the standard planform library in Python 3.9
        #"platform release": platform.freedesktop_os_release().get("PRETTY_NAME", "N/A"),
        "user": os.environ.get("USER", "N/A"),
        "ip_addresses": os.popen("hostname -I").read().strip(),
    }

def main():
    info = get_platform_runtime_info()
    print("Runtime Information:")
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()

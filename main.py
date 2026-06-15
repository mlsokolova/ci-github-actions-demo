import os
import platform

def get_platform_runtime_info():
    return {
        "python_version": os.popen("python --version").read().strip(),
        "os": os.uname().sysname,
        "architecture": os.uname().machine,
        "kernel release": platform.release(),
        "full system info": platform.platform(),
        "platform release": platform.freedesktop_os_release().get("PRETTY_NAME", "N/A"),
        "container": os.environ.get("CONTAINER", "N/A"),
        "cloud_provider": os.environ.get("CLOUD_PROVIDER", "N/A"),
        "ip_addresses": os.popen("hostname -I").read().strip(),
    }

def main():
    info = get_platform_runtime_info()
    print("Runtime Information:")
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()

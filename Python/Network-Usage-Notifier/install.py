import pip

_all_ = ["psutil",]

windows = ["win10toast",]

posix = ["notify2", "dbus-python",]

def install(packages):
    for package in packages:
        pip.main(['install', package])

if __name__ == '__main__':

    import os

    install(_all_)
    if os.name == 'posix':
        install(posix)
    else:
        install(windows)

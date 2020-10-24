import pip

_all_ = ["psutil",]

windows = ["win10toast",]

posix = ["notify2", "dbus-python",]

def install(packages):
    for package in packages:
        pip.main(['install', package])

if __name__ == '__main__':

    from sys import platform

    install(_all_)
    if platform == 'windows':
        install(windows)
    else:
        install(posix)

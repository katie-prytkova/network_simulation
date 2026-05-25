from pyats.easypy import run
import sys


def main():
    run(testscript='tests/test_network_device.py')
    run(testscript='tests/test_router.py')
    run(testscript='tests/test_switch.py')


if __name__ == "__main__":
    main()

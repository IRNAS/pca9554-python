"""
Pca 9554 basic usage example
"""
import time

import pca9554


def example():
    # init
    i2c_address = 0x20
    pca_driver = pca9554.Pca9554(i2c_address)

    # enable pins 0 and 1 to be inputs
    pca_driver.write_config_port(0, pca9554.INPUT)
    pca_driver.write_config_port(1, pca9554.INPUT)

    # enable all others to be outputs
    for i in range(2, 8):
        pca_driver.write_config_port(i, pca9554.OUTPUT)

    # supposedly, a sensor is connected to input 0 or 1 (or both), so values can be read from it

    # read values in a loop
    for _ in range(0, 20):
        value_0 = pca_driver.read_port(0)
        value_1 = pca_driver.read_port(1)
        print("Port 0: {}, Port 1: {}".format(value_0, value_1))

        # wait a bit
        time.sleep(1)


if __name__ == '__main__':
    example()

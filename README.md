# Pca9554 driver

Python driver for PCA9554 for RPi and other devices

## Basic usage

Initialize by providing devices I2C address

```python3
i2c_address = 0x20
pca_driver = pca9554.Pca9554(i2c_address)
```

Set output/input mode of ports (8 ports total are available)

```python3
pca_driver.write_config_port(0, pca9554.INPUT)
pca_driver.write_config_port(3, pca9554.OUTPUT)
```

 Read values from ports

 ```python3
value_0 = pca_driver.read_port(0)
value_1 = pca_driver.read_port(1)
```

For other functionality see [pca9554.py](pca9554.py)

# License

Firmware and software originating from this repository is licensed under the [GNU General Public License v2.0](./LICENSE).

Open-source licensing means the hardware, firmware, software and documentation may be used without paying a royalty, and knowing one will be able to use their version forever. One is also free to make changes, but if one shares these changes, they have to do so under the same conditions they are using themselves. The name IRNAS is a mark of IRNAS LTD. This name and term may only be used to attribute the appropriate entity as required by the Open Licence referred to above. The names and marks may not be used in any other way, and in particular may not be used to imply endorsement or authorization of any hardware one is designing, making or selling.

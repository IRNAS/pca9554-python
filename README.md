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

import spidev
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000
to_send = [0x01, 0x02, 0x03]
spi.xfer(to_send)

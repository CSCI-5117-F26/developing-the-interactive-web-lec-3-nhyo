import time
from halo import Halo

spinner = Halo(text="Loading...", spinner="dots",color="red")

spinner.start()
time.sleep(10)
spinner.stop()
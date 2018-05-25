__version__ = "0.1"
import os

def run(**args):
	version = "0.1"
	print("[*] In environment module.")
	return str(os.version)

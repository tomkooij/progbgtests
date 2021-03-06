import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib

def before():
	try:
		import matplotlib
		matplotlib.use("Agg")
		import matplotlib.pyplot as plt
		plt.switch_backend("Agg")
		lib.neutralizeFunction(plt.pause)
	except ImportError:
		pass

def after():
	try:
		import matplotlib.pyplot as plt
		plt.switch_backend("TkAgg")
		importlib.reload(plt)
	except ImportError:
		pass


@t.test(0)
def correctDistance(test):
	test.test = lambda : (assertlib.numberOnLine(10.86, lib.getLine(lib.outputOf(_fileName), 0), deviation = 0.02) or assertlib.numberOnLine(10860, lib.getLine(lib.outputOf(_fileName), 0), deviation = 20))
	test.description = lambda : "print de afgelegde afstand"

# @t.test(1)
# def showsGraph(test):
# 	test.test = lambda : assertlib.fileContainsFunctionCalls(_fileName, "savefig") or assertlib.fileContainsFunctionCalls(_fileName, "show")
# 	test.description = lambda : "slaat een grafiek op, of laat een grafiek zien"

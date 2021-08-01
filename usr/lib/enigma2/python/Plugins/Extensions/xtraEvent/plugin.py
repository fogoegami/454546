from Plugins.Plugin import PluginDescriptor
from Components.config import config
import threading
from . import xtra
from . import download

def ddwn():
	if config.plugins.xtraEvent.timerMod.value == True:
		download.downloads("").save()
	if config.plugins.xtraEvent.timerMod.value == True:
		tmr = config.plugins.xtraEvent.timer.value
		t = threading.Timer(3600 * int(tmr), ddwn) # 1h=3600
		t.start()


if config.plugins.xtraEvent.timerMod.value == True:
	threading.Timer(30, ddwn).start()


def main(session, **kwargs):
	try:
		session.open(xtra.xtra)
	except:
		import traceback
		traceback.print_exc()


def Plugins(**kwargs):
	return [PluginDescriptor(name="xtraEvent", description="xtraEvent plugin for Open Vision", where=PluginDescriptor.WHERE_PLUGINMENU, icon="plugin.png", fnc=main)]

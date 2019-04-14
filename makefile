default: regen

regen:
	python regen.py

restoration:
	python regen.py sewardRestoration sewardRestoration/sewardRestoration.html

publish_bainbridgeIslandSouth:
	scp bainbridgeIslandSouth.html paulshannnon@pshannon.net:public_html/pshannon.net/swordFerns/regionalMap/bainbridgeIslandSouth/index.html


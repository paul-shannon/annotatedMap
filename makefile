# source ~/github/slexil/tests/pshannon-py363/bin/activate

default: region

region:
	python regen.py regional.2020 tmp.html
	open tmp.html


regen:
	python regen.py

restoration:
	python regen.py sewardRestoration sewardRestoration/sewardRestoration.html

publish_bainbridgeIslandSouth:
	scp bainbridgeIslandSouth.html paulshannnon@pshannon.net:public_html/pshannon.net/swordFerns/regionalMap/bainbridgeIslandSouth/index.html


al:
	python regen.py  regionalSwordFernDieOff/import/map.alSmith alsmith.html

publish_al:
	scp alsmith.html paulshannnon@pshannon.net:public_html/pshannon.net/swordFerns/regionalMap/

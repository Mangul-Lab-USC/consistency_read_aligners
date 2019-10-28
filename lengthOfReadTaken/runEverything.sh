#!/bin/bash
python buildRef.py
python shortReadGenerator.py
python fileTranslator.py
cat Final.txt

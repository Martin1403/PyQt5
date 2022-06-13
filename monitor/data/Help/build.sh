#!/usr/bin/env bash
python -m nuitka --onefile main.py \
--enable-plugin=pyqt5 \
--include-data-file=./data/movies/intro.gif=./data/movies/intro.gif \
--include-data-dir=./etc/=./etc/ \
-o gui
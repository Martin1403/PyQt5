#!/usr/bin/env bash
pyuic5 src/untitled.ui -o src/untitled.py
pyrcc5 data/icons/images.qrc -o images_rc.py

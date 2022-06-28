Recorder
======== 
### Venv:
######  python3.9
###### /recorder
```
python -m venv .venv && \
source .venv/bin/activate && \
pip install -U pip && \
pip install -r requirements.txt
```
### Apt:
```
apt-get -y install \
    portaudio19-dev \
    libportaudio2 \
    libportaudiocpp0 \
    libasound-dev
```
### Run:
###### /recorder
```
python main.py
```
### Convert:
```
pyuic5 src/untitled.ui -o src/untitled.py && \
pyrcc5 data/icons/images.qrc -o images_rc.py && \
python main.py
```
### One-file:
```
python -m nuitka --onefile main.py \
    --enable-plugin=pyqt5 \
    --include-data-file=./data/movies/intro.gif=./data/movies/intro.gif \
    --include-data-dir=./etc/=./etc/ \
    -o gui
```
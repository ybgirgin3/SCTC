## for ubuntu 18.04 <

**required packages**
- [scrot-1.6](https://github.com/resurrecting-open-source-projects/scrot)(do not install from apt it's older version)





- using conda (recommended)
```sh
$ conda install -c conda-forge tesseract-ocr \
  conda install -c conda-forge dbus-python \
  pip3 install -r requirements.txt
```

- using apt
```sh
$ sudo apt install tesseract-ocr \
  sudo apt install python3-dbus \
  pip3 install -r requirements.txt
```

- using brew
```sh
$ brew install tesseract \
  brew install d-bus
  pip3 install -r requirements.txt
```

## download pre-trained data
**for english**
```sh
wget https://github.com/tesseract-ocr/tessdata/raw/master/eng.traineddata
wget https://github.com/ZER-0-NE/EAST-Detector-for-text-detection-using-OpenCV/raw/master/frozen_east_text_detection.pb
```






# SCREENSHOT TO CLIPBOARD FOR LINUX & MACOS

**for tracking the application future please see:**[TODO](TODO.md)

## USAGE:

- run getSS.py file from terminal using python3

```sh
 $ python3 getSS.py         # to get text to clipboard
 $ python3 getSS.py --save  # only save image
```

- draw rectangle to target area
- and done..

## INSTALLATION

**for ubuntu >= 18.04 & Mac**

**required packages**

- [scrot-1.6](https://github.com/resurrecting-open-source-projects/scrot) (apt includes older version do NOT use it, if your system already have it simply uninstall and install this 🙃)


**- using conda (recommended)**
**if you are using conda, don't forget to keep your conda environment active whole installation process**

```sh
$ conda install -c conda-forge tesseract-ocr \
  conda install -c conda-forge dbus-python \
  sudo apt install libimlib2-dev \
  pip3 install -r requirements.txt
```

**- using apt**

```sh
$ sudo apt install tesseract-ocr \
  sudo apt install python3-dbus \
  sudo apt install libimlib2-dev \
  pip3 install -r requirements.txt
```

**- using brew**

```sh
$ brew install tesseract \
  brew install d-bus \
  sudo apt install libimlib2-dev \
  pip3 install -r requirements.txt
```
## AUTO CONFIG
simply run installer.py file 😃 and it's need to be done..

## MANUAL CONFIG
create config.py and paste (you can see my own path in config.py file)

```
tess_path = "<your tesseract installation path>"
save_path = "<pictures folder>"

```

> to get tesseract bin path for linux
>
> ```sh
> $ which tesseract
> ```

create your sctc file like this:

```sh
<path/to/your/python> <absolute/path/of/this/dir/getSS.py>
```

and then you can use SCTC globally





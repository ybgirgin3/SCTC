## for ubuntu >= 18.04 & Mac

**required packages**

- [scrot-1.6](https://github.com/resurrecting-open-source-projects/scrot) (apt includes older version do NOT use it)

**- using conda (recommended)**

```sh
$ conda install -c conda-forge tesseract-ocr \
  conda install -c conda-forge dbus-python \
  pip3 install -r requirements.txt
```

**- using apt**

```sh
$ sudo apt install tesseract-ocr \
  sudo apt install python3-dbus \
  pip3 install -r requirements.txt
```

**- using brew**

```sh
$ brew install tesseract \
  brew install d-bus \
  pip3 install -r requirements.txt
```

and then run

```sh
$ python3 getSS.py
```

create config.py and paste

```
tess_path = "tesseract bin path"

```

> to get tesseract bin path for linux
>
> ```sh
> $ which tesseract
> ```

# Description
Follow the steps below to install OpenCV 4 on Raspberry Pi

## Soucre
Intial scripts and steps from [here](https://gist.github.com/willprice/abe456f5f74aa95d7e0bb81d5a710b60), modified with steps from [pyimagesearch](https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/)

## Steps
```bash
$ chmod +x *.sh
$ ./download-opencv.sh
$ ./install-deps.sh
$ ./build-opencv.sh
$ cd ~/opencv/opencv-4.1.2/build
$ sudo make install
```
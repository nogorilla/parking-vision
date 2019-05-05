# Install OpenCV 4 on macOS
[Source](https://www.pyimagesearch.com/2018/08/17/install-opencv-4-on-macos/)

## Step 1: Install Xcode
To install Xcode, fire up the Apple App Store, find the Xcode app, and install.
After Xcode has installed we need to accept a license agreement. Launch a terminal and enter the following command:
```
sudo xcodebuild -license
```
To accept the license, simply scroll down and accept it.

Once you’ve accepted the license agreement, let’s install Apple Command Line Tools. This is required, so that you’ll have `make` , `gcc` , `clang` , etc. You can install the tools via:
```
sudo xcode-select --install
```

## Step 2: Install Homebrew
For this step we’re going to install the Mac community package manager, Homebrew.
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Update Homebrew definitions:
```
brew update
```

Edit your bash profile with nano using the following command:
```
nano ~/.bash_profile
```

Once you’re actively editing the file, append the following lines to the end to update your `PATH` :
```
# Homebrew
export PATH=/usr/local/bin:$PATH
```

From there, save the profile. If you’re using nano, you’ll see the shortcut keys at the bottom of the window which demonstrate how to save (write) and exit.

Once you’re back in bash, source your bash profile:
```
source ~/.bash_profile
```

## Step #3: Install OpenCV prerequisites using Homebrew
In this section we’ll ensure that Python 3.7 is installed. We’ll also install prerequisites for building OpenCV from source.

### Install Python 3.7
Install python via Homebrew
```
brew install python3
```

Verify the correct version:
```
python3 --version
```

### Install other prerequisites
OpenCV requires a few prerequisites to be installed before we compile it. These packages are related to either (1) tools used to build and compile, (2) libraries used for image I/O operations (i.e., loading various image file formats from disk such as JPEG, PNG, TIFF, etc.) or (3) optimization libraries.

To install these prerequisites for OpenCV on macOS execute the following commands:
```
brew install cmake pkg-config
brew install jpeg libpng libtiff openexr
brew install eigen tbb
brew install wget
```

## Step #4: Install Python dependencies for OpenCV 4
We’re going to install the Python dependencies for OpenCV 4 in this step.

Taking advantage of the `wget` tool that we just installed, let’s download and install pip (a Python package manager):
```
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py
```

Install `virtualenv` and `virtualenvwrapper`, then do a bit of cleanup:
```
sudo pip3 install virtualenv virtualenvwrapper
sudo rm -rf ~/get-pip.py ~/.cache/pip
```

From there, we need to edit our bash profile again so that these two tools work properly. Edit your `bash_profile` as above:
```
# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

### Create virtualenv
```
mkvirtualenv pv -p python3
```

Activate the environment:
```
workon pv
```

install NumPy:
```
pip install numpy
```

## Step #5: Compile OpenCV 4 for macOS
Compiling from source gives you the most control over your build as opposed to package managers such as pip, Homebrew, and Anaconda.

### Download OpenCV 4
Download both the `opencv` and `opencv_contrib` code:
```
cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.1.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.1.0.zip
```

From there, unzip the archives:
```
unzip opencv.zip
unzip opencv_contrib.zip
```

And rename for clarity:
```
mv opencv-4.0.0 opencv
mv opencv_contrib-4.0.0 opencv_contrib
```

### Compile OpenCV4 from source
```
cd ~/opencv
mkdir build && cd !$
```

Now we’re ready for CMake. Be sure to use the  workon  command before executing the cmake  command as shown:
```
workon cv
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D PYTHON3_LIBRARY=`python -c 'import subprocess ; import sys ; s = subprocess.check_output("python-config --configdir", shell=True).decode("utf-8").strip() ; (M, m) = sys.version_info[:2] ; print("{}/libpython{}.{}.dylib".format(s, M, m))'` \
    -D PYTHON3_INCLUDE_DIR=`python -c 'import distutils.sysconfig as s; print(s.get_python_inc())'` \
    -D PYTHON3_EXECUTABLE=$VIRTUAL_ENV/bin/python \
    -D BUILD_opencv_python2=OFF \
    -D BUILD_opencv_python3=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D BUILD_EXAMPLES=ON ..
```

Provided that your CMake output is good to go you can kick off the
compilation via:
```
make -j4
```

If you’ve reached 100%, then there is one additional command to install OpenCV 4:
```
sudo make install
```

## Step #6: Sym-link OpenCV 4 on macOS to your virtual environment site-packages
Before we make a symbolic link to link OpenCV 4 into our Python virtual environment, let’s determine our Python version:

```
workon pv
python --version
> Python 3.6
```

At this point, your Python 3 bindings for OpenCV should reside in the following folder:
```
/usr/local/opt/opencv/lib/python3.7/site-packages/cv2.cpython-36m-darwin.so
```

Rename the file:
```
cd /usr/local/opt/opencv/lib/python3.7/site-packages/
sudo mv cv2.cpython-36m-darwin.so cv2.so
```

Our last sub-step is to sym-link our OpenCV cv2.so  bindings into our `pv` virtual environment:
```
cd ~/.virtualenvs/cv/lib/python3.2/site-packages/
ln -s /usr/local/opt/opencv/lib/python3.7/site-packages/cv2.so cv2.so
```

## Step #7: Test your macOS + OpenCV 3 install
```
$ workon pv
$ python
>>> import cv2
>>> cv2.__version__
'4.1.0'
>>> exit()
```
# install Python3 
sudo apt-get update \
  && sudo apt-get install -y python3-pip python3-dev python3-tk wget \
  && cd /usr/local/bin \
  && sudo ln -s /usr/bin/python3 python \
  && sudo pip3 install --upgrade pip

# create USER sinobot and needed directories
sudo mkdir -p /media/data || true && \

# install OpenCV 4.0
sudo apt-get install -y build-essential cmake unzip pkg-config libgtk2.0-dev
sudo apt-get install -y libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install -y libxvidcore-dev libx264-dev
sudo apt-get install -y libatlas-base-dev gfortran
sudo apt-get install -y poppler-utils poppler-data
sudo apt-get install -y imagemagick imagemagick-6-common imagemagick-6.q16
cd /tmp && wget -O opencv.zip https://github.com/opencv/opencv/archive/4.0.0.zip
cd /tmp && wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.0.0.zip
cd /tmp && unzip opencv.zip && unzip opencv_contrib.zip
cd /tmp && mv opencv-4.0.0 opencv && mv opencv_contrib-4.0.0 opencv_contrib
sudo pip install numpy
mkdir -p /tmp/opencv/build
cd /tmp/opencv/build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D INSTALL_C_EXAMPLES=OFF \
      -D OPENCV_EXTRA_MODULES_PATH=/tmp/opencv_contrib/modules \
      -D PYTHON_EXECUTABLE=/usr/local/bin/python \
      -D BUILD_EXAMPLES=ON .. 
cd /tmp/opencv/build && make -j4 
cd /tmp/opencv/build && sudo make install
cd /tmp/opencv/build && sudo ldconfig
cd /usr/local/lib/python3.6/dist-packages && \
    sudo ln -s /usr/local/python/cv2/python-3.6/cv2.cpython-36m-x86_64-linux-gnu.so cv2.so

# install Tesseract 4.0
sudo apt-get install -y tesseract-ocr

# install all required python libs
sudo pip install -r requirements.txt

# sudo usermod -a -G vboxsf luhya

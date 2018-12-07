### Step 1
```
# build image 
docker-compose build
```
### run server
```
# option 1
docker-compose start/stop/restart

# option 2
docker-compose up -d
```

# options 3

docker run -dit --name test_api -v /home/luhya/src/XinYiRecognition:/usr/local/XinYiRecognition -v /home/luhya/src/xyapi_ws:/usr/local/xyapi_ws  -v /media/data:/media/data -v /var/log/sinyi:/var/log/sinyi -v /home/luhya/src/xyapi_ws/deploy/xyapi.conf:/etc/supervisor/conf.d/xyapi.conf -v /home/luhya/src/xyapi_ws/deploy/chi_xy_hanzi.traineddata:/usr/share/tesseract-ocr/4.00/tessdata/chi_xy_hanzi.traineddata sinyi_api bash

**說明:**

**顯示速度遠遠跟不上影片真實速度，所以使用後製加速(跟重影來緩解閃爍)演飾**

------------


Demo:

| 20x16 | https://youtu.be/GQvvPxIW_Ng |
| ------------ | ------------ |
| 40x32 | https://youtu.be/BFyd2hqgJzY |


------------



因為此LCD螢幕只能使用8個自訂符號，在20x16分辨率下為4x2格剛剛好可以輸出一幀，而40x32分辨率下一排40個像素剛好使用8格，所以使用逐行顯示4行

此Script是給像Bad Apple這樣純黑白的(才能轉換成點陣開與關)的影片，分辨率直接為螢幕輸出像素(20x16/40x32)，基本上只要影片是黑白的就可以正常播放(也要有其他這樣的影片啦)

在40x32下播放可能就算後製加速還是會有閃爍的感覺，這時候可以加入重影


------------


**依賴:**

| RPLCD | `pip3 install RPLCD`  |
| ------------ | ------------ |
| opencv | `pip3 install opencv-python` |


------------


**接線:
**

| Raspberry  | I2C LCD |
| ------------ | ------------ |
| GPIO2 (5V) | VCC |
| GPIO9 (GND) | GND |
| GPIO3 (SDA) | SDA |
| GPIO5 (SCL) | SCL |

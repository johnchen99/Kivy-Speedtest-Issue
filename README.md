I am trying out a simple speedtest application to learn Kivy and speedtest-cli (https://pypi.org/project/speedtest-cli/). The speedtest.py code has output successful speed test result on PC.

The implementation is as simple as a button and importing speedtest.py script. The speedtest.py has been modified mainly on the outputs. However, buildozer's implementation on my Android phone (Android Version 9) doesn't render any errors, yet, the function returned "Cannot retrieve speedtest configuration" found in Line 1870 from shell() in speedtest.py instead.

Seems like Speedtest object has been failed to be initialised.

https://stackoverflow.com/questions/67118888/speedtest-cli-implementation-on-kivy-works-on-pc-but-not-on-android

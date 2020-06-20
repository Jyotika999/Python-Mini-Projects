
#importing you tube module from pytube library
from pytube import YouTube 

yt = YouTube("https://www.youtube.com/watch?v=zIi_qL6sxtk")

dw = yt.streams.get_by_itag(22)

dw.download("Videos/")
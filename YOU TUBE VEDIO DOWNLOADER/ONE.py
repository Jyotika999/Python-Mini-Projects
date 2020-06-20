
#importing you tube module from pytube library
from pytube import YouTube 

yt = YouTube("https://www.youtube.com/watch?v=UT58ETAj3cg")

#using yt.streams.all() , you will be able to get the return of all the streams that may be available for that particular vedio
print(yt.streams.all()) # this prints all the features and the properties of that you tube vedio entered 
print(yt.title) # this will print the title of the youtube vedio you have mentioned the link of 

# each youtube vedio has a unique itag 

print(yt.streams.get_by_itag(22))
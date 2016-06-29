# Download image from 4chan

Easily download images from 4chan

![py4chan](https://1.bp.blogspot.com/-0IozCoKz7gk/U_uEf7dQppI/AAAAAAAALCc/xs6Fx5L4S24/s1600/vivian_james.jpg)

### How to use: 

```python
# entre with board and thread number
c = chandownloader('sp','69046803')

# validate the url
c.verific_url()

# searching images in tread 
c.get_links_content()

# clean duplicate links, always use
c.clear_Link()

# create directory
c.creat_dir()

print (c)

Out: Board: /sp/ 
     Thread: 69046803 
     Url: https://boards.4chan.org/sp/thread/69046803 
     I found 5 images in Thread

# Download images
c.download_images()
Out: 1467152220290.jpg 
     [################################] 20/20 - 00:00:00
     1467152565680.jpg 
     [################################] 22/22 - 00:00:00
     1467154452257.png 
     [################################] 303/303 - 00:00:00
     1467154701557.png 
     [################################] 944/944 - 00:00:01
     1467154899017.jpg 
     [################################] 13/13 - 00:00:00

```

### Requeriments

    * requests==2.10.0
    * clint==0.5.1

![license](https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/GPLv3_Logo.svg/2000px-GPLv3_Logo.svg.png)

![4chan](http://img04.deviantart.net/f67e/i/2014/096/7/3/4chan_logo_vector__transparent_background__by_wize_kevn-d7da8ts.png)

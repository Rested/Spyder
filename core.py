# -*- coding: utf-8 -*-
import urllib
import getpass
import re
import os
import time
#needs youtube-dl and ffmpeg

#Add bug reporting feature.
i=0
un = str(getpass.getuser())
try:
    pathf = open('/home/'+un+'/.pathf.txt', 'r')
except IOError:
    pathf = open('/home/'+un+'/.pathf.txt', 'w')
    mpath= raw_input('Enter the path of the folder you want to put the music files in: ')
    vpath= raw_input('Enter the path of the folder you want to put the video files in: ')
    pathf = open('/home/'+un+'/.pathf.txt', 'a')
    pathf.write(' ' + mpath + ' ' + vpath)
yorn = raw_input('Would you like to change the location you want to put the files in?(y or n): ')
if yorn == 'y':
    mpath= raw_input('Enter the path of the folder you want to put the music files in: ')
    vpath= raw_input('Enter the path of the folder you want to put the video files in: ')
    pathf = open('/home/'+un+'/.pathf.txt', 'a')
    pathf = open('/home/'+un+'/.pathf.txt', 'a')
    pathf.write(' ' + mpath + ' ' + vpath)
pathf = open('/home/'+un+'/.pathf.txt', 'r')
pfl =  pathf.read().split()
print len(pfl)
mpath = pfl[len(pfl)-2]
vpath = pfl[len(pfl)-1]
print mpath + ' ' + vpath
while i >= 0:
    if i > 0:
        print 'Please enter a value.'
    try:
        ispeed = int(raw_input('Type youtube-dl http://www.youtube.com/watch?v=Bc5xb6Ftfd8 into terminal and find download speed. Enter here(k(b)/s): '))
        break
    except ValueError:
        i=i+1

print 'Are there any specific songs you\'d like to download now?',
ans = raw_input('(y or n):')
stl=[]
while ans == 'y':
    print 'Specify what you\'d like to search youtube for:',
    st = raw_input()
    st = st.replace('(', '').replace(')', '').replace('&', 'and').replace('.','').replace('\'','')
    stl.append(st)
    ans = raw_input('Would you like to dl another song? (y or n)')
while i < len(stl):
    j=0
    live='live'
    regex = "id=\"translate_link_([--z]*)\""
    regex2 = "title>([ -z]*)</title"
    regex3 = "ion\" content=\"([ -z]*)\">"
    mp3search = urllib.urlopen("http://www.youtube.com/results?search_query="+stl[i].replace(' ','+')) 
    html1 = mp3search.read()
    html1 = html1.replace('&#39;','\'').replace('%27','\'')#etc try to make it so wierd chars work unlike now due to html encoding
    mp3search.close
    failcount=0
    vidid = re.search(regex, str(html1.replace('&#39;', '\'')))
    #print tracklist[i] + ' ' + artistlist[i]
    while 'live' in live.lower() and 'live' not in stl[i].lower():
        if j > 0:
            html1 = html1.replace(vidid.group(0), '')#.replace('&#39;','\'')
            vidid = re.search(regex, str(html1))
        j=j+1
        #try:
        vid = urllib.urlopen("http://www.youtube.com/watch?v="+vidid.group(1))
        html2 = vid.read().replace('\n', '').replace('&#39;','\'').replace('&quot;','').replace('- YouTube','')
        livet = re.search(regex2, str(html2))
        lived = re.search(regex3, str(html2))
        ltg1 = str(livet.group(1))
        if lived != None:
            live = ltg1 + ' ' + ltg1
        else:
            live = ltg1
        #means to ensure at least some of track title is in yt title
        k=0
        l=0
        while len(stl[i].split()) > k:
            if str(stl[i].split()).lower()[k] not in ltg1.lower().replace('lyrics',''):
                l=l+1
                if  len(stl[i].split())-l < 2:
                    live='live'
                    print ltg1
            k=k+1
        #except AttributeError:
        #print 'May be a live version...'
        #break
    print 'Metadata for '+stl[i]+':'
    ti = raw_input('Title: ')
    ar = raw_input('Artist: ')
    al = raw_input('Album: ')
    t1= time.time()
    os.system('youtube-dl -o '+vpath+str(stl[i]).replace(' ', '_').replace('/','')+'.flv \"http://www.youtube.com/watch?v='+vidid.group(1)+'\"')
    #print 'http://www.youtube.com/watch?v='+vidid.group(1)
    print '.',
    os.system('ffmpeg -i '+vpath+stl[i].replace(' ', '_').replace('/','')+'.flv -f mp3 -acodec libmp3lame -ab 192k -metadata title=\"'+ti.replace('/','')+'\" -metadata author=\"'+ar.replace('/','')+'\" -metadata album=\"'+al.replace('/','')+'\" '+mpath+stl[i].replace(' ', '_')+'.mp3')
    print '.'
    t2 = time.time()
    if int(t2-t1) < 4:
        print str(stl[i]) + ' failed to download.'
    i = i+1
    
print 'Copy and paste your spotify playlist into a .txt file and save it as ' + vpath + 'spurl.txt'
raw_input('Press enter when done. ')

tracklist = []
artistlist = []
albumlist = []
urllisttemp = []
urllist = open(vpath + 'spurl','r').read().split()
try:
    dlurls = open(vpath + 'dlurls.txt', 'r')
except IOError:
    dlurls = open(vpath + 'dlurls.txt', 'w')
    dlurls = open(vpath + 'dlurls.txt', 'r')    
i=0

dlurlsstr = dlurls.read()

while i < len(urllist):
    if urllist[i] not in dlurlsstr:
        urllisttemp.append(urllist[i])
    i=i+1    
urllist=urllisttemp


    
i = 0
tlf = open(vpath+'tlf.txt', 'a')
try:
    atlf = open(vpath+'atlf.txt', 'r')
except IOError:
    atlf = open(vpath+'atlf.txt', 'w')
    atlf = open(vpath+'atlf.txt', 'r')
alf = open(vpath+'alf.txt', 'a')
allf = open(vpath+'allf.txt', 'a')
dlurls = open(vpath +'dlurls.txt', 'a')
atlfstr = atlf.read()

print '\n'

while i < len(urllist): 
    try:
        site = urllib.urlopen(urllist[i])
        html = site.read()
        site.close
        rawstr = "<title>(.*) by (.*) on ([ -z]*)</title>"
        htmla = re.search(rawstr, str(html))
        if htmla != None:
            track = htmla.group(1)
            artist = htmla.group(2)
            if str(track+artist) not in atlfstr:
                try:
                    allf.write(re.search("href=\".*album.*>([ -z]*)<", str(html)).group(1).replace(',',' ')+',')
                    tlf.write(track.replace(',',' ') + ',')
                    alf.write(artist.replace(',',' ') + ',')
                    dlurls.write(urllist[i]+' ')
                except AttributeError:
                    print urllist[i] + ' failed. Please report URL.'
        else:
            print 'URL: ' + str(urllist[i]) + ' failed. May be local?'
    except IOError:
        try:
            print 'Connection problem. Will reattempt after 1 minute...'
            time.sleep(60)
            site = urllib.urlopen(urllist[i])
            html = site.read()
            site.close 
            rawstr = "<title>(.*) by (.*) on ([ -z]*)</title>"
            htmla = re.search(rawstr, str(html))
            if htmla != None:
                track = htmla.group(1)
                artist = htmla.group(2)
                if str(track+artist) not in atlfstr:
                    try:
                        allf.write(re.search("href=\".*album.*>([ -z]*)<", str(html)).group(1).replace(',',' ')+',')
                        tlf.write(track.replace(',',' ') + ',')
                        alf.write(artist.replace(',',' ') + ',')
                        dlurls.write(urllist[i]+' ')
                    except AttributeError:
                        print urllist[i] + ' failed. Please report URL.'
            else:
                print '\nURL: ' + str(urllist[i]) + ' failed. May be local?'
        except IOError:
            print 'Connection failed. Try again later.'
            exit(0)
        
    i=i+1
    print '.',

dlurls = open(vpath + 'dlurls.txt', 'r')
tlf = open(vpath+'tlf.txt', 'r')
alf = open(vpath+'alf.txt', 'r')
allf = open(vpath+'allf.txt', 'r')

tracklist=tlf.read().split(',')
del tracklist[len(tracklist)-1]
artistlist=alf.read().split(',')
del artistlist[len(artistlist)-1]
albumlist=allf.read().split(',')
del albumlist[len(albumlist)-1]

i = 0

while i < len(tracklist):
        if '&#39;' in tracklist[i] or '&#39;' in artistlist[i] or '&#39;' in albumlist[i]:
            tracklist[i] = tracklist[i].replace('&#39;', '\'')
            artistlist[i] = artistlist[i].replace('&#39;', '\'')
            albumlist[i] = albumlist[i].replace('&#39;', '\'')
        if '&amp;' in tracklist[i] or '&amp;' in artistlist[i] or '&amp;' in albumlist[i]:
            tracklist[i] = tracklist[i].replace('&amp;', 'and')
            artistlist[i] = artistlist[i].replace('&amp;', 'and')
            albumlist[i] = albumlist[i].replace('&amp;', 'and')
        if 'é' in tracklist[i] or 'é' in artistlist[i] or 'é' in albumlist[i]:
            tracklist[i] = tracklist[i].replace('é', 'e')
            artistlist[i] = artistlist[i].replace('é', 'e')
            albumlist[i] = albumlist[i].replace('é', 'e')
        tracklist[i] = tracklist[i].replace('.', '')
        artistlist[i] = artistlist[i].replace('.', '')
        albumlist[i] = albumlist[i].replace('.', '')
        tracklist[i] = tracklist[i].replace('(', '')
        artistlist[i] = artistlist[i].replace('(', '')
        albumlist[i] = albumlist[i].replace('(', '')
        tracklist[i] = tracklist[i].replace(')', '')
        artistlist[i] = artistlist[i].replace(')', '')
        albumlist[i] = albumlist[i].replace(')', '')
        tracklist[i] = tracklist[i].replace('/', '')
        artistlist[i] = artistlist[i].replace('/', '')
        albumlist[i] = albumlist[i].replace('/', '')
        i=i+1

i=0
while i < len(tracklist):
    if str(tracklist[i]+artistlist[i]) in atlfstr:
        del tracklist[i]
        del artistlist[i]
        del albumlist[i]
        i=i-1
    i=i+1

print 'Will take roughly: ' + str(((float(len(tracklist))*11)/(float(ispeed)/1000))/60) + ' minutes to download.'
print 'About ' + str((float(len(tracklist))*11)/100) + ' Gigabytes will be downloaded.'
i=0
while i < len(tracklist):
    atlf = open(vpath+'atlf.txt', 'a')
    j=0
    live='live'
    regex = "id=\"translate_link_([--z]*)\""
    regex2 = "title>([ -z]*)</title"
    regex3 = "ion\" content=\"([ -z]*)\">"
    mp3search = urllib.urlopen("http://www.youtube.com/results?search_query="+tracklist[i].replace(' ','+')+'+'+artistlist[i].replace(' ','+')) 
    html1 = mp3search.read()
    html1 = html1.replace('&#39;','\'').replace('%27','\'')#etc try to make it so wierd chars work unlike now due to html encoding
    #print html1
    mp3search.close
    failcount=0
    vidid = re.search(regex, str(html1.replace('&#39;', '\'')))
    #print tracklist[i] + ' ' + artistlist[i]
    while 'live' in live.lower() and 'live' not in tracklist[i].lower() and 'live' not in artistlist[i].lower():
        if j > 0:
            html1 = html1.replace(vidid.group(0), '')#.replace('&#39;','\'')
            vidid = re.search(regex, str(html1))
        j=j+1
        try:
            vid = urllib.urlopen("http://www.youtube.com/watch?v="+vidid.group(1))
            html2 = vid.read().replace('\n', '')
            livet = re.search(regex2, str(html2))
            lived = re.search(regex3, str(html2))
            if lived != None:
                live = livet.group(1) + ' ' + lived.group(1)
            else:
                live = livet.group(1)
            #means to ensure at least some of track title is in yt title
            k=0
            l=0
            while len(tracklist[i].split()) > k:
                if tracklist[i].split()[k] not in livet.group(1):
                    l=l+1
                    if  len(tracklist[i].split())-l < 2:
                        live='live'
                k=k+1
        except AttributeError:
                if failcount==0:
                    failcount=1
                    mp3search = urllib.urlopen("http://www.youtube.com/results?search_query="+tracklist[i].replace(' ','+')+'+'+artistlist[i].replace(' ','+')+'&page=2')
                    html1 = mp3search.read()
                    print html1
                    mp3search.close
                    print 'Trying page 2'
        else:
            break
        
    t1= time.time()
    print tracklist[i] + ' by ' + artistlist[i] + ' downloading.',    
    
    os.system('youtube-dl -o '+vpath+tracklist[i].replace(' ', '_').replace('/','')+'.webm \"http://www.youtube.com/watch?v='+vidid.group(1)+'\"')
    print '.',
    os.system('ffmpeg -i '+vpath+tracklist[i].replace(' ', '_').replace('/','')+'.webm -f mp3 -acodec libmp3lame -ab 192k -metadata title=\"'+tracklist[i].replace('/','')+'\" -metadata author=\"'+artistlist[i].replace('/','')+'\" -metadata album=\"'+albumlist[i].replace('/','')+'\" '+mpath+tracklist[i].replace(' ', '_')+'.mp3')
    print '.'
    t2 = time.time()
    if int(t2-t1) > 4:
        atlf.write(tracklist[i]+artistlist[i])
    i = i+1
    atlf = open(vpath+'atlf.txt', 'r')



##def converttoletterlist(thestr):
##    #does as above ^
##    mystr = thestr
##    mylist = []
##    while len(mystr) > 0:
##        toad = mystr[:1] + mystr[len(mystr):]
##        mystr = mystr[:0] + mystr[1:]
##        mylist.append(toad)
##    return mylist

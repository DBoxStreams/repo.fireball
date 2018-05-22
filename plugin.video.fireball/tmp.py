def WRZCRAFT_CATS(url):

    u = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
    match = re.compile('<img src="(.+?)" alt="(.)(.*?)" title=.+?</strong>.+?<a href="(.+?)" class="more-link">',re.DOTALL).findall(u)
    for image,first,rest,url2 in match:
        name = ('[B][COLOR dimgrey]' + first + '[/COLOR][COLOR darkred]' + rest +'[/COLOR][/B]')
        iconimage = image.encode('utf-8')
        name = name.replace('Watch','').replace('Download','').replace('online','').encode('utf-8').lstrip()
        addLink(name,url2,325,iconimage,fanart)
    np = re.compile("<a class=\"nextpostslink\" rel=\"next\" href=\"(.+?)\">&raquo;</a>").findall(u)
    for nextpage in np:	
        addDir('Next Page -->',nextpage,324,icon,fanart)

def WRZCRAFT_LINKS(name,url):

    xbmc.executebuiltin("ActivateWindow(busydialog)")

    r = open_url(url)
    r = re.compile('<a href="(.+?)"').findall(r)# + re.compile('<span style="color: #008000;"><strong>(.+?)</strong>',re.DOTALL).findall(r)
    #prer = re.compile('<a href="(.+?)(filefactory|nitroflare|rapidgator)(.+?)(mkv|avi|mp4|flv|mkv\.html|avi\.html|mp4\.html|flv\.html)" rel="nofollow">').findall(r)# + re.compile('<span style="color: #008000;"><strong>(.+?)</strong>',re.DOTALL).findall(r)
    #for http,source,file,end in prer:
        #r = http + source + file + end
    #if '.rar' not in p:
    #    r = p
    if len(r) == 0: quit()
    elif len(r) >= 1:
        streamurl=[]
        streamname=[]
        a = 0
        for b in r:
            b = b.lstrip()
            if '.rar' not in b:
                c = b.lstrip().replace('http://','').replace('https://','').replace('www.','').replace('.com','').replace('.net','').replace('.org','').replace('.co','').replace('.to','')
                d = re.compile('^(.+?)/.+?/.+?/(.+?)(mp4|mkv|rar|html)').findall(c)
            for host,file,type in d:
                if 'mkv' in type:
                    type = 'MKV'
                elif 'mp4' in type:
                    type = 'MP4'
                elif 'rar' in type:
                    type = 'Not A Playable Format'
                elif 'html' in type:
                    type = '?'
                e = '[B][COLOR dimgrey]'+host+'[/COLOR] [COLOR white]|[/COLOR] [COLOR yellow]'+type+'[/COLOR] [COLOR white]|[/COLOR] [COLOR darkred]'+file+'[/COLOR][/B]'
            if urlresolver.HostedMediaFile(b).valid_url():
                a += 1
                streamurl.append(b)
                streamname.append('%s' % str(e))
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        if len(streamurl) == 1: PLAYLINK(name,streamurl[0],icon)
        else:
            dialog = xbmcgui.Dialog()
            select = dialog.select(name,streamname)
            if select < 0:
                quit()
            else:
                PLAYLINK(name,streamurl[select],icon)
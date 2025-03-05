import os
def delete_data():
    path = 'D:\\project1204\\python爬虫\\爬qq音乐\\歌曲下载\\'
    dir=os.listdir(path)
    lis = []
    for i in dir:
        lis.append(i)

    for k in lis:
        fr = open('D:\\project1204\\python爬虫\\爬qq音乐\\歌曲下载\\'+'%s'%k,'rb')
        if not fr.read():
            fr.close()
            os.remove('D:\\project1204\\python爬虫\\爬qq音乐\\歌曲下载\\'+'%s'%k)
            print('{}为付费歌曲(无法完整下载:获取不到完整的purl )===================请期待程序升级  该程序已自动为您删除空白文件'.format(k))
        else:
            fr.close()
            continue

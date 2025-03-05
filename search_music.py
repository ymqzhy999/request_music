import json,os,time,sys
from 爬qq音乐 import dele #自动删除空白资源
import requests
# import user_view

headers = {

    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Origin': 'https://y.qq.com',
    'Referer': 'https://y.qq.com/portal/search.html',
}


def get_music_info():
    music_info_list = []
    name= input('请输入歌手或歌曲：')
    page = input('请输入页码：')
    num = input('请输入当前页码需要返回的数据条数：')
    url = f'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p={page}&n={num}&w={name}'

    time.sleep(2)
    print('正在获取歌曲信息字典 ===== 请等待')
    response = requests.get(url).text  # 获取到的是字符串
    print('====ok====')
    # 将response切分成json格式 类似字典 但是现在还是字符串
    music_json = response[9:-1] #截取字典那部分 数据类型仍然是字符串
    # json转字典
    music_data = json.loads(music_json)  # 转换成 字典类型
    # print(music_data)
    music_list = music_data['data']['song']['list']
    """
    list列表里每个元素的样式
    {'albumid': 8036, 'albummid': '000y5gq7449K9I', 'albumname': '第二天堂', 'albumname_hilight': '第二天堂',
     'alertid': 2, 'belongCD': 0, 'cdIdx': 6, 'chinesesinger': 0, 'docid': '1943774058310078813', 'grp': [], 
     'interval': 267, 'isonly': 0, 'lyric': '', 'lyric_hilight': '', 'media_mid': '003NikJo0a0uzm', 'msgid': 15, 
     'newStatus': 2, 'nt': 4294516403, 'pay': {'payalbum': 0, 'payalbumprice': 0, 'paydownload': 1, 'payinfo': 1, 
     'payplay': 1, 'paytrackmouth': 1, 'paytrackprice': 200}, 'preview': {'trybegin': 83866, 'tryend': 119107, 'trysize': 960887},
      'pubtime': 1086278400, 'pure': 0, 'singer': [{'id': 4286, 'mid': '001BLpXF2DyJe2', 'name': '林俊杰', 
      'name_hilight': '<em>林俊杰</em>'}], 'size128': 4288455, 'size320': 10720847, 'sizeape': 0, 'sizeflac': 31386542,
       'sizeogg': 6600445, 'songid': 9063002, 'songmid': '004TXEXY2G2c7C', 'songname': '江南', 'songname_hilight': '江南', 
       'strMediaMid': '003NikJo0a0uzm', 'stream': 1, 'switch': 16881409, 't': 1, 'tag': 11, 'type': 0, 'ver': 0, 'vid': 'b0013k1imsl'},
    """
    for music in music_list:
            music_name = music['songname']  # 歌曲的名字
            singer_name = music['singer'][0]['name']  # 歌手的名字
            songmid = music['songmid']
            music_info_list.append((music_name, singer_name, songmid, ))
    return music_info_list


# 获取vkey
def get_purl(music_info_list):
    music_data = []
    for music in music_info_list:
        music_name = music[0]
        singer_name = music[1]#inc
        songmid = music[2]
        url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"8846039534","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"8846039534","songmid":["%s"],"songtype":[0],"uin":"1152921504784213523","loginflag":1,"platform":"20"}},"comm":{"uin":"1152921504784213523","format":"json","ct":24,"cv":0}}' % songmid

        time.sleep(1)
        response = requests.get(url).json()  # 如果你获取的数据 是 {}  .json() 他会直接帮我们转换成字典
        # print(response)
        purl = response['req_0']['data']['midurlinfo'][0]['purl']
        print('将携带{}songmid的data传入网址 获取结果 提取purl--->{}'.format(music_name, purl))
        full_media_url = 'http://dl.stream.qqmusic.qq.com/' + purl
        music_data.append({
                'music_name': music_name,
                'singer_name': singer_name,
                'full_media_url': full_media_url}
        )
    return music_data


def save_music_mp3(music_data):
    if not os.path.exists('歌曲下载'):  # 判断是否有歌曲下载文件夹
        os.mkdir('歌曲下载')  # 如果没有创建 歌曲下载文件夹
    for music in music_data:
        music_name = music['music_name']
        singer_name = music['singer_name']
        full_url = music['full_media_url']
        music_response = requests.get(full_url, headers=headers).content
        #由于是音频要将爬取的内容.content转为二进制
        with open(r"C:\Users\ymq\Desktop\qq音乐%s-%s.mp3" % (music_name, singer_name), 'wb+')as fp:
            #'歌曲下载/%s-%s.mp3'
            time.sleep(0.1)
            print('无损音质下载中')
            fp.write(music_response)
            try:
                var = sys.getsizeof(r'C:\Users\ymq\Desktop\qq音乐%s-%s.mp3' % (music_name, singer_name))
                print('=========={}下载成功======消耗内存{}MB'.format(music_name,var/40))


            except:
                print('内存获取错误')

if __name__ == '__main__':
    music_info_list = get_music_info()
    music_data = get_purl(music_info_list)
    save_music_mp3(music_data)
    dele.delete_data()







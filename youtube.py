
import requests
import pytomo.start_pytomo as start_pytomo
import pytomo.config_pytomo as config_pytomo



config_pytomo.LOG_FILE = '-'
file_name = 'somefile.txt'

def get_most_popular_video():
    res = requests.get('https://www.googleapis.com/youtube/v3/videos?'
                  'chart=mostPopular&'
                  'key=AIzaSyAE5NngJQOE40hLqjRtIr0GP5j9BFFF-Kw&'
                  'part=id&'
                  'maxResults=50&'
                       'regionCode=FI'
                  )
    most_pop_list = res.json()['items']
    with open('somefile1.txt', 'a') as the_file:
        for each in most_pop_list[0:24]:
            the_file.write('https://www.youtube.com/watch?v=' + each['id']+'\n')
    with open('somefile2.txt', 'a') as the_file:
        for each in most_pop_list[25:49]:
            the_file.write('https://www.youtube.com/watch?v=' + each['id'] + '\n')

## log_file = start_pytomo.configure_log_file(timestamp)
if __name__ == '__main__':
    #config_pytomo.DATABASE = 'result'
    #get_most_popular_video()
    config_pytomo.BATCH_MODE = True
    config_pytomo.INPUT_FILE = 'somefile1.txt'

    start_pytomo.main()
    config_pytomo.INPUT_FILE = 'somefile2.txt'
    start_pytomo.main()





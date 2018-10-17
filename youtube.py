import pytomo.start_pytomo as start_pytomo
import pytomo.config_pytomo as config_pytomo



config_pytomo.LOG_FILE = '-'
file_name = 'test.txt'


## log_file = start_pytomo.configure_log_file(timestamp)
if __name__ == '__main__':
    #config_pytomo.DATABASE = 'result'
    config_pytomo.INPUT_FILE = file_name
    config_pytomo.BATCH_MODE = True
    start_pytomo.main()
    print start_pytomo.timestamp




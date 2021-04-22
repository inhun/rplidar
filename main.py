import logging
import time
import cv2

from lidar_iter import RPLidar
from video_capture import BufferlessVideoCapture


def init_logger():
    '''
    Initiate main logger.
    '''
    _logger = logging.getLogger('Main')
    _logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    _logger.addHandler(stream_handler)
    return _logger 


if __name__ == '__main__':

    logger = init_logger()

    lidar = RPLidar('COM11')
    cap = BufferlessVideoCapture(1)
    
    time.sleep(1)
    img_num = 0
    while True:
        
        try:
            ret, frame = cap.read()
            if ret:
                err, data = lidar.read()
                if err:
                    
                    now = time.strftime('%H%M%S', time.localtime(time.time()))
                    with open(f'data/distance/{now}.txt', 'w') as f:
                        f.write('{}\n'.format(data))

                    cv2.imwrite(f'data/images/{now}.jpg', frame)
                    img_num +=1
                time.sleep(1)
        
        except KeyboardInterrupt:
            logger.info('keyboardinterrupt')
            cap.thr.do_run = False
            lidar.thr.do_run = False
            lidar.stop()
            lidar.disconnect()
            logger.info('finish')
            exit()
        

        
    lidar.stop()
    lidar.disconnect()
    
    
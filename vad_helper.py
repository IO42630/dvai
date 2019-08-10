import pyaudio


def print_all_device_info():
    """
    :return: Prints the info of all the device as seen by PyAudio()
    """
    pa = pyaudio.PyAudio()
    sb = ""
    for i in range(0, pa.get_device_count()):
        b = pa.get_device_info_by_index(i)
        sb+='index: ' + str(b['index'])+'  '
        sb+='sampleRate: '+ str(b['defaultSampleRate'])+'  '
        sb+='name: '+ b['name']+'\n'
    print(sb)



if __name__ == '__main__':
    print_all_device_info()

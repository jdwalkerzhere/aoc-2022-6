from utils import detect

if __name__ == '__main__':
    with open('stream.txt','r') as stream:
        stream = stream.readline().strip('\n')
    
    print(detect(stream, 4))
    print(detect(stream, 14))
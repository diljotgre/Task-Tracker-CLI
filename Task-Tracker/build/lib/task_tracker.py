import argparse

def main():
    parser = argparse.ArgumentParser(description="Task Tracker")
    parser.add_argument('--name', type=str, help='your name please')

    parser.add_argument('--friend', type=str, help ="your friend's name")


    args = parser.parse_args()


    print()
    

if __name__=='__main__':
    main()




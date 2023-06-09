from extract import main as extract_main
from transform import main as transform_main
from load import main as load_main
def main():
    extract_main()
    transform_main()

if __name__=='__main__':
    main()
    # load_main()

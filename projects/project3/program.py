from misc_files.BistroSystem import BistroSystem
from misc_files.password_authenticate import authenticate


def main():
    authenticate()
    bistro_system = BistroSystem()
    bistro_system.start()

if __name__ == '__main__':
    main()

from MyQR import myqr
import os


def main():
    version, level, qr_name = myqr.run(
        words="I Love You",
        version=1,
        level="H",
        picture="./file/source.gif",
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name="l.gif",
        save_dir="./file/"
    )


if __name__ == '__main__':
    main()

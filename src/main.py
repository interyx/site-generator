from src.util import *
from src.generator import *


def main():
    copy_dir(
        "/home/interyx/dev/site-generator/static",
        "/home/interyx/dev/site-generator/public",
        True,
    )

    generate_pages_recursive(
        "/home/interyx/dev/site-generator/content/",
        "/home/interyx/dev/site-generator/template.html",
        "/home/interyx/dev/site-generator/public/",
    )


if __name__ == "__main__":
    main()

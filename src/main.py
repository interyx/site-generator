from src.util import *
from src.generator import *


def main():
    copy_dir(
        "/home/interyx/dev/site-generator/static",
        "/home/interyx/dev/site-generator/public",
        True,
    )

    generate_page(
        "/home/interyx/dev/site-generator/content/index.md",
        "/home/interyx/dev/site-generator/template.html",
        "/home/interyx/dev/site-generator/public/index.html",
    )


if __name__ == "__main__":
    main()

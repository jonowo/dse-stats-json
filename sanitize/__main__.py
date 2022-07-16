import logging

from sanitize import sanitize_general, sanitize_subjects

logging.basicConfig(
    level="INFO",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def main():
    sanitize_general()
    sanitize_subjects()


if __name__ == "__main__":
    main()

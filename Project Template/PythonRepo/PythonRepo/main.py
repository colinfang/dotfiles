import argparse
import logging

LOGGER = logging.getLogger(__name__)

def main():
    fmt = '%(levelname)s - %(name)s - %(message)s'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - {}'.format(fmt)
    )

    parser = argparse.ArgumentParser()
    parser.add_argument('--api_key', required=True)

    args = parser.parse_args()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        # Exception goes to logger handler e.g. Sentry
        LOGGER.exception('Something went wrong')
        raise

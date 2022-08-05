from subprocess import Popen

from logger import get_logger

logger = get_logger(__name__)


def popen_wait(command: list):
    """
    - Popen直前でコマンドを出力
    - wait後にprocessのreturncodeを出力
    """
    logger.info(f'Popen({" ".join(command)})')
    process = Popen(command)
    process.wait()
    logger.info(f'process.returncode: {process.returncode}')


def main():
    # returncode: 0 -> 正常
    popen_wait(['ls', '-al'])

    # returncode: 7 -> エラー
    popen_wait(['curl', 'http://localhost:3000'])


if __name__ == '__main__':
    main()

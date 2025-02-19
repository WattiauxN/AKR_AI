import argparse
from core.loader.load_provider import LoadProvider
import sys

# arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--File", default="default", type=str, help="...")
parser.add_argument("-s", "--save", help="...", action="store_true")
parser.add_argument("-S", "--Save", help="...")

loader = LoadProvider('provider.mp3.MP3Provider')
mp3 = loader.cached_import('MP3Provider')
print(sys.modules)

instance = mp3("/home/user/workspace/akr/data/Accenteur_mouchet.mp3")
instance.load()

if __name__ == "__main__":
    args = parser.parse_args()
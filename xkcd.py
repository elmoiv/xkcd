from urllib.request import urlopen, urlretrieve
import os

os.makedirs('XKCD', exist_ok=True)
os.chdir('XKCD')

# Getting main info to get total images count
info = eval(urlopen(f'https://xkcd.com/info.0.json').read())

BIG_N = int(info['num'])
IMAGES = os.listdir()
CODE = True
N = 0

print(f'xkcd has {BIG_N} images')

while N < BIG_N:
    N += 1

    # xkcd real-life meme, lol XD
    if N == 404:
        continue

    # Check if this one exists
    if any(
        map(
            lambda i: i in IMAGES,
            '{}.jpg {}.png {}.gif {}.jpeg'.format(*[N] * 4).split()
            )
        ):
        continue

    try:
        # Get image url from API instead of parsing [Faster]
        json = eval(urlopen(f'https://xkcd.com/{N}/info.0.json').read())

        img_url = json['img']

        # Check if url has no comic (Magic comic)
        if img_url.endswith('/comics/'):
            print(f'No comic at: {N}')
            continue

        # Decide extension and name
        ext = img_url.split('.')[-1]
        img_name = f'{N}.{ext}'

        # Download image
        urlretrieve(
            img_url,
            img_name
            )

        print(f'Saved: {img_name}')

    # Catch error and inform user
    except BaseException as e:
        print(f'Error at {N}: {e}')
        continue

print('Finished :)')
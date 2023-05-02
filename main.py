# Test python env
def print_hello():
    animals = ['dog', 'cat', 'hamster'] # in one line
    foods = [
        'man',
        'woman'
    ]# w/ trailling comma
    names = [
        'john',
        'jane',
        'gill'
    ]# w/ trailling comma
    for f_name in names:
        print(f'hello, {f_name}')

if __name__ == '__main__':
    print_hello()

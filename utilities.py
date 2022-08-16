def coloured(seq):
    colors = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m'
    }

    tmpStr = ''

    for n in seq:
        if n in colors:
            tmpStr += colors[n] + n
        else:
            tmpStr += colors['reset'] + n
        
    return tmpStr + '\033[0;0m'
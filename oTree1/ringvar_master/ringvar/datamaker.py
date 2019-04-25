import random, json

def make_block(p, n):
    """Returns a block, i.e., n samples of a Bernoulli distribution of probability p."""
    samples = []
    for _ in range(n):
        samples.append( 1 if random.random() < p else 0 )
    return {'p':p, 'samples':samples}

def make_blockset(N, n, minp=0.001, maxp=0.999):
    """Make a blockset, i.e., a list of N blocks of n samples, with randomized probabilities.
    N will be the number of blocks one subject sees.
    (and N*n the number of rings they see)."""
    r = []
    for _ in range(N):
        p = random.uniform(minp, maxp)
        r.append( make_block(p, n) )
    return r

def make_blocksets(M,N,n, minp=0.001, maxp=0.999):
    '''Make M blocksets, each containing N blocks of n samples.
    M should be comparable to the number of subjects.'''
    r = []
    for _ in range(M):
        r.append( make_blockset(N,n, minp, maxp) )
    return r

def make_and_save_blocksets(M,N,n,filename, minp=0.001, maxp=0.999):
    blocksets = make_blocksets(M,N,n, minp, maxp)
    f = open(filename, 'w')
    json.dump(blocksets, f)
    f.close()

def load_blocksets(filename):
    f = open(filename, 'r')
    blocksets = json.load(f)
    f.close()
    return blocksets


from simulation import DiscoverySimulation

SECONDS_PER_SLOT = 0.625 * 10**(-6)

factor = 300
def genrange(minarg, maxarg, step):
    """
    Generator for range 
    """
    k = minarg
    while k <= maxarg:
        yield k
        k += step

def parameterGenerator():
    """
    Generator for all valid parameter set tuples (P in paper)
    """
    MS = 10**(-3)

    for T in genrange(20*MS, 10.24, 0.625*MS * factor):  # Scanning Interval
        for Ts in genrange(20*MS, 10.24, 0.625*MS * factor):                      # Scanning Window
            for Ta in genrange(20*MS, 10.24, 0.625*MS * factor):
                if Ts <= T:
                    yield (T, Ts, Ta)

def calc_mean_for_param(paramset, samples=1000):
    #print(paramset)
    (T, Ts, Ta) = paramset

    Tslots = T/SECONDS_PER_SLOT
    Tsslots = Ts/SECONDS_PER_SLOT
    Taslots = Ta/SECONDS_PER_SLOT

    # 20 Bytes / 1MBit/s
    advlength = (20*8) / 1000000
    advlengthslots = advlength/SECONDS_PER_SLOT
    blengthslots = (0.01 - advlength)/SECONDS_PER_SLOT

    randomslots = 0.01/SECONDS_PER_SLOT

    sim = DiscoverySimulation(Tslots, Tsslots, Taslots, advlengthslots, blengthslots, randomslots)
    mean = sim.mean(samples=samples)

    #return mean

    return ((T, Ts, Ta), (mean[0] * SECONDS_PER_SLOT, mean[1] * SECONDS_PER_SLOT), mean[2])




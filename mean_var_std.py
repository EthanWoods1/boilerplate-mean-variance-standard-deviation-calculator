import numpy as np

def calculate(list):

    arr = np.array(list)
    arr2D = arr.reshape(3,3)

    def helper(type=None):
        if type == "flat":
            return ( np.mean(arr), np.var(arr),
                     np.std(arr), np.max(arr),
                     np.min(arr), np.sum(arr) )
        elif type == "axis0":
            return ( np.mean(arr, axis=0), np.var(arr, axis=0),
                     np.std(arr, axis=0), np.max(arr, axis=0),
                     np.min(arr, axis=0), np.sum(arr, axis=0) )
        else:
            return ( np.mean(arr, axis=1), np.var(arr, axis=1),
                     np.std(arr, axis=1), np.max(arr, axis=1),
                     np.min(arr, axis=1), np.sum(arr, axis=1) )

    flat_stuff = helper("flat")
    axis0_stuff = helper("axis0")
    axis1_stuff = helper("axis1")

    calculations = {'mean': [ axis0_stuff[0], axis1_stuff[0], flat_stuff[0] ]
                    'variance': [ axis0_stuff[1], axis1_stuff[1], flat_stuff[1] ]
                    'standard deviation': [ axis0_stuff[2], axis1_stuff[2], flat_stuff[2] ]
                    'max': [ axis0_stuff[3], axis1_stuff[3], flat_stuff[3] ]
                    'min': [ axis0_stuff[4], axis1_stuff[4], flat_stuff[4] ]
                    'sum': [ axis0_stuff[5], axis1_stuff[5], flat_stuff[5] ]
                    }

    return calculations
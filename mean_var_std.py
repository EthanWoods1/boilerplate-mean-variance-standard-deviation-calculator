import numpy as np

def calculate(list):

    if len(list)<9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list)

    try:
        np.sum(arr)
    except:
        raise ValueError("Not all elements are numbers!")

    arr2D = arr.reshape(3,3)

    def helper(type=None):
        if type == "flat":
            return ( np.mean(arr), np.var(arr),
                     np.std(arr), np.max(arr),
                     np.min(arr), np.sum(arr) )
        elif type == "axis0":
            return ( np.mean(arr2D, axis=0), np.var(arr2D, axis=0),
                     np.std(arr2D, axis=0), np.max(arr2D, axis=0),
                     np.min(arr2D, axis=0), np.sum(arr2D, axis=0) )
        else:
            return ( np.mean(arr2D, axis=1), np.var(arr2D, axis=1),
                     np.std(arr2D, axis=1), np.max(arr2D, axis=1),
                     np.min(arr2D, axis=1), np.sum(arr2D, axis=1) )

    flat_stuff = helper("flat")
    axis0_stuff = helper("axis0")
    axis1_stuff = helper("axis1")

    calculations = {'mean': [ axis0_stuff[0].tolist(), axis1_stuff[0].tolist(), flat_stuff[0].item() ],
                    'variance': [ axis0_stuff[1].tolist(), axis1_stuff[1].tolist(), flat_stuff[1].item() ],
                    'standard deviation': [ axis0_stuff[2].tolist(), axis1_stuff[2].tolist(), flat_stuff[2].item() ],
                    'max': [ axis0_stuff[3].tolist(), axis1_stuff[3].tolist(), flat_stuff[3].item() ],
                    'min': [ axis0_stuff[4].tolist(), axis1_stuff[4].tolist(), flat_stuff[4].item() ],
                    'sum': [ axis0_stuff[5].tolist(), axis1_stuff[5].tolist(), flat_stuff[5].item() ]
                    }

    return calculations

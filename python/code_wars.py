import math

def triangular_range(start, stop):
        dict = {}
            ans = 0;
                for i in range(start, stop + 1):
                            ans = (math.sqrt(1 - (4 * (i * -2))) - 1) * 0.5
                                    if ans == int(ans):                                                    dict[int(ans)] = i

return dict

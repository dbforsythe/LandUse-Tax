import sys
sys.argv = ['SFR','125000']
landuse = sys.argv[0]
value = int(sys.argv[1])


def taxcalc(landuse, value):
    if landuse == "SFR":
        rate = 0.05
    elif landuse == "MFR":
        rate = 0.04
    else:
        rate = 0.02
        assessment = value * rate
        return assessment

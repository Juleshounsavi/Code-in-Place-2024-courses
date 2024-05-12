"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""
C = 299792458
def main():
    m=float(input("Enter kilos of mass:"))
    E = m*(C**2)
    print("e = m * C^2...")
    print("m = {} kg".format(m))
    print("C = {} m/s".format(C))
    print("{} joules of energy!.".format(E))

if __name__ == '__main__':
    main()
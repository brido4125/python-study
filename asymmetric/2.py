Pcurve = 2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1  # The proven prime
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141  # Number of points in the field
Acurve = 0;
Bcurve = 7  # These two defines the elliptic curve. y^2 = x^3 + Acurve * x + Bcurve
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
GPoint = (Gx, Gy)  # This is our generator point. Trillions of dif ones possible

# Individual Transaction/Personal Information


private_key = 0x1e99423a4ed27608a15a2616a2b0e9e52ced330ac530edcc32c8ffc6a526aedd


# 역원 구하기
def get_inversion(a, n=Pcurve):  # Extended Euclidean Algorithm/'division' in elliptic curves
    lm, hm = 1, 0
    low, high = a % n, n
    while low > 1:
        ratio = high / low
        nm, new = hm - lm * ratio, high - low * ratio
        lm, low, hm, high = nm, new, lm, low
    return lm % n


def ECadd(a, b):  # Not true addition, invented for EC. Could have been called anything.
    LamAdd = ((b[1] - a[1]) * get_inversion(b[0] - a[0], Pcurve)) % Pcurve
    x = (LamAdd * LamAdd - a[0] - b[0]) % Pcurve
    y = (LamAdd * (a[0] - x) - a[1]) % Pcurve
    return (x, y)


def ECdouble(a):  # This is called point doubling, also invented for EC.
    Lam = ((3 * a[0] * a[0] + Acurve) * get_inversion((2 * a[1]), Pcurve)) % Pcurve
    x = (Lam * Lam - 2 * a[0]) % Pcurve
    y = (Lam * (a[0] - x) - a[1]) % Pcurve
    return (x, y)


def EccMultiply(GenPoint, ScalarHex):  # Double & add. Not true multiplication
    ScalarBin = str(bin(ScalarHex))[2:]
    Q = GenPoint
    for i in range(1, len(ScalarBin)):  # This is invented EC multiplication.
        Q = ECdouble(Q);  # print "DUB", Q[0]; print
        if ScalarBin[i] == "1":
            Q = ECadd(Q, GenPoint);  # print "ADD", Q[0]; print
    return Q


PublicKey = EccMultiply(GPoint, private_key)
print(PublicKey)

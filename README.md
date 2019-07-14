# private-and-public-key
Implementation of private and public key
---------------------------------------
---------------------------------------
**consider one scenerio**
#Choose 2 prime numbers (big) : X, Y
N = X * Y
Maximum message length we can encrypt is log(N)
Z = (Y – 1) * (X – 1)
Find E coprime to Z (that is gcd(Z,E) = 1)
Find D such as D*E=1 mod Z
E and D are the private and public keys
Encrypt using (message ^ E) mod N and
Decrypt using (message ^ D) mod N

#Example with numbers (very simple):

y=5
X=11
N = Y*X =55
k<log(55) = 5 – maximum message length is 5 bit
Z=(Y-1)*(X-1)=40
E=13
D=37
D*E=481 => 481 mod 40 = 1
If we want to send the message ‘11010’ (26)

We are using the public key (13)
26^13 mod 55 = 31 (‘11111’)
send ‘11111’ to the other side
The other side has the private key (37)
31^37 mod 55 = 26
Using PyCrypto First we generate the key pair

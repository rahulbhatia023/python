print(bin(25))
# 0b11001
# The bin() method converts and returns the binary equivalent string of a given integer. If the parameter isn't an
# integer, it has to implement __index__() method to return an integer
# The prefix 0b represents that the result is a binary string.

print(0b11001)
# 25

print(oct(25))
# 0o31
# The oct() method takes an integer number and returns its octal representation.

print(hex(25))
# 0x19
# The hex() method takes an integer number and returns its hexadecimal representation.

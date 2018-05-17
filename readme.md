# Polloard's rho attack on Elliptic curve
Given P, a point on ellpitic curve,
we could find k such that kG=P, where G is base point of ellpitic curve
The complexity of algorithm takes $$O(\sqrt{n})$$ time.
We have define 32,36,40,44,48,52,56 bits order of ellpitic curve,

### Execution
After installing the required package, you can simply excute as following: 
Usage: python pollards_rho_attack.py select_bits iterations
```sh
$ python pollards_rho_attack.py 40bits 10
```
Iterations mean how many P you want to break,
for different computer, you can measure complexity of algorithm by recording total steps of algorithm
or you can record time cost on your machine


def test(first, *args, **kwargs):
   print(first)
   print(args)
   print(kwargs)

test(1, 2, 3, 4, k1=5, k2=6, k3=7)
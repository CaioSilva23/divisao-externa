l = {'x':[('11/2022', '13/2022', '34/2022', '88/2022', '31/2022', '14/2022', '13/2022', '56/9888', '21/2022', '16/22', '17/2022'),
            (164962.27, 10000.0, 56000.0, 8999.0, 20000.0, 67000.0, 223111.0, 500000.0, 723000.0, 1000000.0, 900000.0),
            (5000.0, 5000.0, 18000.0, 6000.0, 9000.0, 14999.0, 52000.0, 49999.0, 10000.0, 0, 0),
            (159962.27, 5000.0, 38000.0, 2999.0, 11000.0, 52001.0, 171111.0, 450001.0,713000.0, 1000000.0, 900000.0),
            ('3.03', '50.00', '32.14', '66.67', '45.00', '22.39', '23.31', '10.00', '1.38', '0.00', '0.00')]}

for i in l.values():
    print(i[1])
    for k, j in enumerate(i):
        print(j[k])
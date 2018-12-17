if __name__ == '__main__':
    ans = 0
    for i in range(57):
        for j in range(i+1,58):
            for k in range(j+1,59):
                for l in range(k+1,60):
                    ans +=(2*i+1)*(2*j+1)*(2*k+1)*(2*l+1)
    print ans
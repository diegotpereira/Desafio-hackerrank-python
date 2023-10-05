from anagram import anagram

# if __name__ == '__main__':
    
#     numeroTestes = int(input().strip())
    
#     for nItr in range(numeroTestes):
        
#         palavra = input()
        
#         resultado = anagram(palavra)
        
#         print(str(resultado) + '\n')


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(str(result) + '\n')
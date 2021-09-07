# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.


def findsum(num):
    ans = 0
    # if(len(str(num)) == 1 or len(str(num)) == 2 ):
    #     ans = num
    # elif(len(str(num)) == 3 or len(str(num)) == 4):
    #     # 99빼고 100부터 num까지
    #     ans = 99
    #     for i in range(100,num+1):
    #         numlist = list(map(int,str(i)))
    #         if((numlist[0]-numlist[1]) == (numlist[1]-numlist[1])):
    #             ans += 1

    for i in range(1, num + 1):
        numlist = list(map(int, str(i)))
        if i < 100:
            ans += 1
        else:
            if ((numlist[0] - numlist[1]) == (numlist[1] - numlist[2])):
                ans += 1
    print(ans)
    return ans


findsum(100)

# 함수 아닌 버전
# num = int(input())
# ans = 0
#
# for i in range(1,num+1):
#     numlist = list(map(int,str(i)))
#     if i<100:
#         ans += 1
#     else:
#         if ((numlist[0] - numlist[1]) == (numlist[1] - numlist[2])):
#             ans += 1
# print(ans)
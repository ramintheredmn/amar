import math

program_vaz = True
# a function that sums all the items in  a list
def sumsum(nums):
    num_1 = 0
    for e in nums:
        num_1 += e
    return num_1
# mohasebeye miyane bar hasb inke tedad item ha zoj bashad ya fard
def miyane(nums):
    nums.sort()
    if len(nums) % 2 == 0:
        # 0  1  2  3  
        #[1, 2, 3, 4, 5, 6] --> len(a) = 6 | 6/2 -1 = 2 --> 2nd index = 3 | 3rd index
        miy = (nums[(len(nums)//2)-1] + nums[(len(nums)//2)]) / 2
    elif len(nums) % 2 != 0:
        miy = nums[(math.ceil(len(nums)/2))-1]

    return miy
def zarzar(nums):
    x_zar = 1
    for x_zar_1 in nums:
        x_zar = x_zar * x_zar_1
    return x_zar

def varians(nums):
    x_bar = (sumsum(nums)/len(nums))
    var = 0
    for number in nums:
        var += ((x_bar - number)**2)

    return var / len(nums)
print ("""
    in yek barname baraye mohasebeye :
    miyangin
    miyane
    varians
    enheraf meyar mibashad.
    tamam hogog mahfoz va motaaleg be 'Redmn' mibashad
    **** LOTFAN DAR VARED KARDAN
    VORODI HA DEGGAT KONID ****

    Telegram : @imraminrd
    instagram : ramin__rafiee

    Good Luck
""")
while program_vaz:
    try:
        q = input("Aya edame midahid? ('bale' , 'kheyr') : ")
        if q == 'kheyr':
            program_vaz = False
        elif q == 'bale':
            program_vaz =True
        else:
            print("vorodi eshtebah (fagat 'bale' ya 'kheyr')")

        while program_vaz:
            # Getting multiple inputs from user
            x = [int(x) for x in input("adad hara vared konid : ").split()]
            print("miyangin : ", (sumsum(x)/len(x)), "\n\n\nmiyane : ",miyane(x),"\n\n\nvarians : ", varians(x), "\n\n\nenheraf meyar : ", math.sqrt(varians(x)), "\n\n\n\nHasel zarbeshan : ", zarzar(x))

            
            a = input("\n\n\nDobare ?  ('bale' , 'kheyr') : ")
            if a == 'kheyr':
                program_vaz = False
            elif a == 'bale':
                program_vaz =True
            else:
                print("vorodi eshtebah (fagat 'bale' ya 'kheyr')")
    except:
        print("Vorodi Eshtebah")

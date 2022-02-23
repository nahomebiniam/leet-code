def removedups(nums):
    x = 1

    for i in range(len(nums)-1):
	    if(nums[i]!=nums[i+1]):
		    nums[x] = nums[i+1]
		    x+=1
    return(x,nums)

nums = [0,0,1,1,1,2,2,3,3,4]
print(removedups(nums))

def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    
    index, step = 0, 1
    output = [''] * numRows
    
    for char in s:
        output[index] += char
        
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
            
        index += step 
        
    return ''.join(output)

print(convert("PAYPALISHIRING", 3))

def reverse(x):
    x = str(x)
    if len(x) == 1:
        return x
    output = ''
    if x[0] == '-':
        output +='-'
        x = x[1:]
        output += x[::-1]
        return int(output)
    else:
        output += x[::-1]
        return int(output)

print(reverse(-123))

def myAtoi(s):
    map = {'1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '0':0}

    output = s.split(" ")
    print(output)
    for char in output:
        if char[0] in map or char[0] == '-':
            return int(char)

print(myAtoi('-123'))

def maxArea(height):
    left, right = 0, len(height) - 1
    size = 0 
    
    for width in range(len(height)-1, 0, -1):
        if height[left] < height[right]:
            size = max(size, width*height[left])
            left += 1
        else:
            size = max(size, width*height[right])
            right -= 1
            
    return size

print(maxArea([4,3,2,1,4]))

def intToRoman(num):
    M=["","M","MM","MMM"]
    C=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    X=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    I=["","I","II","III","IV","V","VI","VII","VIII","IX"]
    
    return M[num//1000]+C[(num//100)%10]+X[(num//10)%10]+I[num%10]

print(intToRoman(1994))

def lengthOfLastWord(s):
    
    output = s.split(' ')
    while '' in output:
        output.remove('')
    return len(output[-1])

print(lengthOfLastWord("luffy is still joyboy"))

def plusOne(digits):
    digits = [str(digi) for digi in digits]
    output = ''.join(digits)
    output = int(output)
    output += 1
    output = str(output)
    return output.split()

print(plusOne([1,2,3]))

# Created By : Sagar Agrawal

# EPAI : Session 11 - Modules

## This repository have following Image processing  modules :

### * J2P.py

#### Description : 

This module takes .jpeg image as input , along with the directory path of the image and converts it into image with extension .png. The image is stored in a new directory named __Converted_to_jpg__

#### Arguments :
Following are the input arguments for this module :

-im / --image_name : Input jpeg image name

-p / --image_path : Input jpeg image folder path


#### Usage : 

To use this module run the following command in terminal :
```
python J2P.py -im image1.jpg -p ./images
```

### * P2J.py

#### Description : 

This module takes .png image as input , along with the directory path of the image and converts it into image with extension .jpeg. The image is stored in a new directory named __Converted_to_jpg__

#### Arguments :
Following are the input arguments for this module :

-im / --image_name : Input jpeg image name

-p / --image_path : Input jpeg image folder path


#### Usage : 

To use this module run the following command in terminal :
```
python P2J.py -im image1.png -p ./images
```

### Question 2.2 : Using list comprehension (and zip/lambda/etc if required) write an expression that strips every vowel from a string provided (tsai>>t s)

```
input_string = 'sagar'

#### An expression that strips every vowel from a string provided
print("".join([x if x.lower() not in ['a', 'e' , 'i' ,'o','u'] else " " for x in input_string]))

#### Output : s g r
```

### Question 2.3 : Using list comprehension (and zip/lambda/etc if required) write an expression that acts like a ReLU function for a 1D array

![](https://www.techvariable.com/wp-content/uploads/2018/11/7nn.png)

```
Relu_input = [random.randint(-100 , 100) for x in range(10)]
print(Relu_input)

#### Clipping the negative inputs and fixing them to zero
print([x if x>0 else 0 for x in Relu_input ])
```

### Question 2.4 : Using list comprehension (and zip/lambda/etc if required) write an expression that acts like a Sigmoid function for a 1D array

![](https://github.com/sagar9926/session7-sagar9926/blob/master/sigmoid.png)

```

Sigmoid_input = [random.random() for x in range(10)]
print(Sigmoid_input)

#### Sigmoid implementation
print([1 / (1 + exp(-x)) if x>0 else 0  for x in Sigmoid_input  ])

```

### Question 2.5 : Using list comprehension (and zip/lambda/etc if required) write an expression that takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn

```
input_string = 'tsai'

#### Expression that takes a small character string and shifts all characters by 5
print("".join([chr(ord(x) + 5 ) if ord(x) <= 117 else chr(96 + 5 - 122 - ord(x))  for x in input_string]))

```

### Question 3 : A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt PTS:200

```
#### Reading the data from file containing Swear texts
f = open("Swear_Words.txt",'r')
Swear_Words = f.read()
f.close()

Swear_Words = set(Swear_Words.split())


#### Reading the data from file containing Paragraph texts
f = open("Paragraph.txt",'r')
Paragraph = f.read()
f.close()

Paragraph = set(Paragraph.split())

#### A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words
print(any([x for x in Swear_Words if x in Paragraph]))

```

### Question 4.1 : Using reduce function add only even numbers in a list.

```
#### Generating a list of random numbers
list1 = [random.randint(0,100) for x in range(10)]
print(list1)

#### Adding only even numbers in a list.
print(reduce(lambda a,b : a + b if b%2 == 0 else a ,list1))

```
### Question 4.2 : Using reduce function find the biggest character in a string.

```
#### Creating randomly a string that contains printable characters
sample_string = "".join([string.printable[random.randint(0,100)] for x in range(10)])
print(sample_string)

#### finding the biggest character in a string.
print(reduce(lambda a,b : a if ord(a) > ord(b) else b ,sample_string))

```

### Question 4.3 : Using reduce funtion add every 3rd number in a list:

```
#### Generate a list with 10 random numbers e.g [10,20,30,40,50,60]
list1 = [random.randint(0,100) for x in range(10)]

#### allocate indexes starting from 1 to every element of the list e.g [(1,10),(2,20),(3,30),(4,40),(5,50),(6,60)]
z = list(zip( list(range(1,len(list1) + 1)) , list1))

#### add every 3rd number in a list : 30 + 60  = 90
print(reduce(lambda a , b : a + b, [item[1] for item in list(filter(lambda  x : True if x[0]%3 == 0 else False ,z))]))

```

### Question 5 : Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999

```
#### Creating a list of all Capital letter alphabets
Alphabets = [chr(x) for x in range(65,91)]

#### Number plate dtaset creation expression
["KA" + str(random.randint(10,99)) + random.choice(Alphabets) + random.choice(Alphabets) + str(random.randint(1000,9999)) for _ in range(15)]

```

### Question 6 : Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided

```
def number_plate_generation(KA, DD, DDDD):
    return([ KA + str(random.randint(10,99)) + random.choice(Alphabets) + random.choice(Alphabets) + str(DDDD) for _ in range(15)])

f = partial(number_plate_generation, DDDD = '1234')
```

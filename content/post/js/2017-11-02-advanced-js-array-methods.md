---
title: "Advanced Javascript Array Methods"
slug: "advanced-array-methods"
date: "2017-11-02"
tags: ["advanced-javascript"]
---


## forEach

1.  Iterates through an array
2.  Runs a callback function on each value in the array
3.  always returns "undefined"

```javascript
var arr = [1,2,3,5]

arr.forEach(function(d,i,arr){
    console.log(d,i);
});
```

1.  How does forEach work

```javascript
var forEach = (arr, callback) => {
    for(var i = 0; i < arr.length; i++) {
        callback(arr[i],i,arr);
    }
}
```

1.  Using forEach in a function

```javascript
var halfValues = (arr) => {
    let newArr = [];
    arr.forEach(function(d){
        newArr.push(d/2);
    })
    return newArr;
}
```

### Coding Ex forEach

```javascript
/*
Write a function called doubleValues which accepts an array and returns a new array with all the values in the array passed to the function doubled

Examples:
    doubleValues([1,2,3]) // [2,4,6]
    doubleValues([5,1,2,3,10]) // [10,2,4,9,20]

*/
function doubleValues(arr){
    let newArr = [];
    arr.forEach(function(d){
        newArr.push(d * 2);
    });
    return newArr;
}

/*
Write a function called onlyEvenValues which accepts an array and returns a new array with only the even values in the array passed to the function

Examples:
    onlyEvenValues([1,2,3]) // [2]
    onlyEvenValues([5,1,2,3,10]) // [2,10]

*/
function onlyEvenValues(arr){
    let newArr = [];
    arr.forEach(function(d){
        if (d%2 === 0) {
            newArr.push(d)
        }
    });
    return newArr;
}

/*
Write a function called showFirstAndLast which accepts an array of strings and returns a new array with only the first and last character of each string.

Examples:
    showFirstAndLast(['colt','matt', 'tim', 'udemy']) // ["ct", "mt", "tm", "uy"]
    showFirstAndLast(['hi', 'goodbye', 'smile']) // ['hi', 'ge', 'se']

*/
function showFirstAndLast(arr){
    let newArr = [];
    arr.forEach(function(d){
        let newVal = d[0]+d.slice(d.length - 1);
        newArr.push(newVal);
    });
    return newArr;
}

/*
Write a function called addKeyAndValue which accepts an array, a key, and a value and returns a the array passed to the function with the new key and value added for each variable 

Examples:
    addKeyAndValue([{name: 'Elie'}, {name: 'Tim'}, {name: 'Matt'}, {name: 'Colt'}], 'title', 'instructor') 

    // [{name: 'Elie', title:'instructor'}, {name: 'Tim', title:'instructor'}, {name: 'Matt', title:'instructor'}, {name: 'Colt', title:'instructor'}]

*/
function addKeyAndValue(arr,key,value){

    arr.forEach(function(d){
        d[key] = value;
    })
    return arr;
}

/*
Write a function called vowelCount which accepts a string and returns an object with the keys as the vowel and the values as the number of times the vowel appears in the string. This function should be case insensitive so a lowercase letter and uppercase letter should count

Examples:
    vowelCount('Elie') // {e:2,i:1};
    vowelCount('Tim') // {i:1};
    vowelCount('Matt') // {a:1})
    vowelCount('hmmm') // {};
    vowelCount('I Am awesome and so are you') // {i: 1, a: 4, e: 3, o: 3, u: 1};
*/
function vowelCount(str){
    var splitArr = str.split("");
    var obj = {};
    var vowels = "aeiou";

    splitArr.forEach(function(letter){
        let newLet = letter.toLowerCase()
        if(vowels.indexOf(newLet)!==-1){
            if(newLet in obj){
                obj[newLet] ++;
            } else {
                obj[newLet] = 1;
            }
        }
    })
    return obj;
}
```

## map

### Definition

1.  create new array
2.  iterates through an array
3.  runs a callback function for each value in the array
4.  adds the result of that callback function to the new array
5.  returns the new array
6.  map always returns a new array of the same length

### example

```javascript
var arr = [1,2,3];

arr.map(function(d,i,array){
    return d ** 2;
})
```

### How does it work?

1.  Creates a new array
2.  Iterates through an array
3.  Runs a callback function for each value in the array
4.  Pushes result of the each callback function to the new array
5.  Returns the new array

```javascript
var myMap = (arr, fn) => {
    let newArr = [];
    arr.forEach(
        function(d,i,oldArr){
            newArr.push(fn(d,i,oldArr));
        }
    )
    return newArr;
}
```

### Use map in a function

#### tripleValue

```javascript
var tripleValues = (arr) => {
    return arr.map(function(d){
        return d * 3;
    })
}
```

#### onlyFirst

```javascript
var onlyFirst = (arr) => {
    return arr.map(function(d){
        return d.first;
    })
}

onlyFirst([{first:"Isaac", last:"Zhou"}, {first:"Raul", last:"Garcia"}])
```

### map Exercises

```javascript
/*
Write a function called doubleValues which accepts an array and returns a new array with all the values in the array passed to the function doubled

Examples:
    doubleValues([1,2,3]) // [2,4,6]
    doubleValues([1,-2,-3]) // [2,-4,-6]
*/

function doubleValues(arr){
    return arr.map(function(val){
        return val * 2;
    })
}

/*
Write a function called valTimesIndex which accepts an array and returns a new array with each value multiplied by the index it is currently at in the array.

Examples:
    valTimesIndex([1,2,3]) // [0,2,6]
    valTimesIndex([1,-2,-3]) // [0,-2,-6]
*/

function valTimesIndex(arr){
    return arr.map(function(d,i){
        return d * i
    })
}

/*
Write a function called extractKey which accepts an array of objects and some key and returns a new array with the value of that key in each object.

Examples:
    extractKey([{name: 'Elie'}, {name: 'Tim'}, {name: 'Matt'}, {name: 'Colt'}], 'name') // ['Elie', 'Tim', 'Matt', 'Colt']
*/

function extractKey(arr, key){
    return arr.map(function(d){
        return d[key]
    })
}

/*
Write a function called extractFullName which accepts an array of objects and returns a new array with the value of the key with a name of "first" and the value of a key with the name of  "last" in each object, concatenated together with a space. 

Examples:
    extractFullName([{first: 'Elie', last:"Schoppik"}, {first: 'Tim', last:"Garcia"}, {first: 'Matt', last:"Lane"}, {first: 'Colt', last:"Steele"}]) // ['Elie Schoppik', 'Tim Garcia', 'Matt Lane', 'Colt Steele']
*/

function extractFullName(arr){
    return arr.map(function(d){
        return d.first+" "+d.last
    })
}
```

## Filter

### Definition

1.  Create a new array
2.  Iterates through an array
3.  Runs a callback function on each value in the array
4.  If the callback function returns
    1.  true: the value will be added to the new array
    2.  false: the value will be ignored from the new array
5.  The results of the callback will always be a boolean

### Example

#### return value greater than 2

```javascript
var arr = [1,2,3];

arr.filter(function(d,i,array){
    return d >=2 ;
})
```

#### return name length greater than 3

```javascript
var instructors = [{name:"Elie"},
                   {name:"Tim"},
                   {name:"Matt"},
                   {name:"Colt"}];

instructors.filter(function(d){
    return d.name.length > 3;
})
```

### How does it work?

1.  Create a new array
2.  Iterates through an array
3.  Runs a callback function on each value in the array
4.  If the callback function returns
    1.  true, the value will be added to the new array
    2.  false, the value will be ignored from the new array

```javascript
var myFilter = (arr, fn) => {
    let newArr = [];
    for(var i = 0; i < arr.length; i++) {
        if (fn(arr[i],i,arr)) {
            newArr.push(fn(arr[i]))
        }
    }
    return newArr;
}
```

### Using filter in a function

#### Only Four Letter names

```javascript
var onlyFourLetterName = function(arr){
    return arr.filter(function(d){
        return d.length === 4;
    });
}

onlyFourLetterName(["Rustiy", "Matt", "Moxie", "Colt"]);
```

#### Divisible by Three

```javascript
var divisibleByThree = function(arr){
    return arr.filter(function(d){
        return d % 3 === 0;
    })
}

divisibleByThree([1,2,3,4,5,6,7,8,9])
```

### Filter Exercises

```javascript
/*
Write a function called filterByValue which accepts an array of objects and a key and returns a new array with all the objects that contain that key.

Examples:
    filterByValue([{first: 'Elie', last:"Schoppik"}, {first: 'Tim', last:"Garcia", isCatOwner: true}, {first: 'Matt', last:"Lane"}, {first: 'Colt', last:"Steele", isCatOwner: true}], 'isCatOwner') // [{first: 'Tim', last:"Garcia", isCatOwner: true}, {first: 'Colt', last:"Steele", isCatOwner: true}]
*/

function filterByValue(arr, key){
    return arr.filter(function(d){
        return d[key]
    })
}

/*
Write a function called find which accepts an array and a value and returns the first element in the array that has the same value as the second parameter or undefined if the value is not found in the array.

Examples:
    find([1,2,3,4,5], 3) // 3
    find([1,2,3,4,5], 10) // undefined
*/

function find(arr, searchValue){
    return arr.filter(function(d){
        return d === searchValue;
    })[0]
}

/*
Write a function called findInObj which accepts an array of objects, a key, and some value to search for and returns the first found value in the arrayt.

Examples:
    findInObj([{first: 'Elie', last:"Schoppik"}, {first: 'Tim', last:"Garcia", isCatOwner: true}, {first: 'Matt', last:"Lane"}, {first: 'Colt', last:"Steele", isCatOwner: true}], 'isCatOwner',true) // {first: 'Tim', last:"Garcia", isCatOwner: true}
*/

function findInObj(arr, key, searchValue){
    return arr.filter(function(d){
        return d[key] === searchValue;
    })[0]
}

/*
Write a function called removeVowels which accepts a string and returns a new string with all of the vowels (both uppercased and lowercased) removed. Every character in the new string should be lowercased.

Examples:
    removeVowels('Elie') // ('l')
    removeVowels('TIM') // ('tm')
    removeVowels('ZZZZZZ') // ('zzzzzz')
*/

function removeVowels(str){
    let strArr = str.split("");
    let newArr = [];
    strArr.filter(function(d){
        if (!"aeiou".split("").includes(d.toLowerCase())) {
            newArr.push(d.toLowerCase())
        }
    })
    return newArr.join("");
}

/*
Write a function called doubleOddNumbers which accepts an array and returns a new array with all of the odd numbers doubled (HINT - you can use map and fitler to double and then filter the odd numbers).

Examples:
    doubleOddNumbers([1,2,3,4,5]) // [2,6,10]
    doubleOddNumbers([4,4,4,4,4]) // []
*/

function doubleOddNumbers(arr){
    let newArr = [];
    arr.filter(function(d){
        if (d%2 !== 0) {
            newArr.push(d*2);
        }
    })
    return newArr;
}
```

## some

### Definition

1.  Iterates through an array
2.  Runs a callback on each value in the array
3.  If the callback returns true for at least one single value, return true
4.  Otherwise return false
5.  The result of the callback will always be a boolean
6.  Similar to the OR logic

### Example

```javascript
var arr = [1,2,3];

arr.some(function(d){
    return d > 4;
}) //false

arr.some(function(d){
    return d > 2;
}) //true
```

### How does it work?

1.  Iterates through an array
2.  Runs a callback on each value in the array
3.  If the callback returns true for at least one single value, return true
4.  Else return false

```javascript
var mySome = function(arr, fn){
    for(var i = 0; i < arr.length; i++) {
        if (fn(arr[i],i,arr)) {
            return true;
        }
    }
    return false;
}
```

### Using some in a function

#### has Even number

```javascript
var hasEvenNumber = (arr) => {
    return arr.some(function(d){
        return d%2 === 0;
    })
}
```

#### Has comma

```javascript
var hasComma = (str) => {
    return str.split("").some(function(d){
        return d === ","
    })
}
```

## every

### Definition

1.  iterate through an array
2.  runs a callback on each value in the array
3.  If the callback returns false fro any single value, return false
4.  Otherwise return true
5.  logic and

### Example

```javascript
var arr = [-1,-2,-3];

arr.every(function(d){
    return d > 0;
}) // false

arr.every(function(d){
    return d < 0;
})
```

### How does it work

1.  Iterates through an array
2.  Runs a callback on each value in the array
3.  If the callback returns false for any single value, return false
4.  Otherwise return true

```javascript
var myEvery = (arr, fn)=>{
    for(var i = 0; i < arr.length; i++) {
        if (!fn(arr[i],i,arr)) {
            return false;
        };
    };
    return true;
}
```

### Use every in a function

#### all lower case

```javascript
var allLowerCase = (str) => {
    return str.split("").every(function(d){
        return d === d.toLowerCase();
    })
}
```

#### all arrays

```javascript
var allArrays = (arr) => {
    return arr.every(Array.isArray);
}
```

### Exercises

```javascript
/*
Write a function called hasOddNumber which accepts an array and returns true if the array contains at least one odd number, otherwise it returns false.

Examples:
    hasOddNumber([1,2,2,2,2,2,4]) // true
    hasOddNumber([2,2,2,2,2,4]) // false
*/

function hasOddNumber(arr){
    return arr.some(function(d){
        return d%2 !== 0;
    })
}

/*
Write a function called hasAZero which accepts a number and returns true if that number contains at least one zero. Otherwise, the function should return false

Examples:
    hasAZero(3332123213101232321) // true
    hasAZero(1212121) // false
*/

function hasAZero(arr){
    // myArr = [arr+""].toString().split("")
    return arr.toString().split("").some(function(d){
        return d === "0";
    })
}

/*
Write a function called hasOnlyOddNumbers which accepts an array and returns true if every single number in the array is odd. If any of the values in the array are not odd, the function should return false. 

Examples:
    hasOnlyOddNumbers([1,3,5,7]) // true
    hasOnlyOddNumbers([1,2,3,5,7]) // false
*/

function hasOnlyOddNumbers(arr){
    return arr.every(function(d){
        return d % 2 !== 0;
    })
}

/*
Write a function called hasNoDuplicates which accepts an array and returns true if there are no duplicate values (more than one element in the array that has the same value as another). If there are any duplicates, the function should return false.

Examples:
    hasNoDuplicates([1,2,3,1]) // false
    hasNoDuplicates([1,2,3]) // true
*/

function hasNoDuplicates(arr){
    return arr.every(function(d){
        return arr.indexOf(d) === arr.lastIndexOf(d);
    })
}

/*
Write a function called hasCertainKey which accepts an array of objects and a key, and returns true if every single object in the array contains that key. Otherwise it should return false.

Examples:
    var arr = [
        {title: "Instructor", first: 'Elie', last:"Schoppik"}, 
        {title: "Instructor", first: 'Tim', last:"Garcia", isCatOwner: true}, 
        {title: "Instructor", first: 'Matt', last:"Lane"}, 
        {title: "Instructor", first: 'Colt', last:"Steele", isCatOwner: true}
    ]

    hasCertainKey(arr,'first') // true
    hasCertainKey(arr,'isCatOwner') // false
*/

function hasCertainKey(arr, key){
    return arr.every(function(d){
        return Object.keys(d).includes(key)
    })
}

/*
Write a function called hasCertainValue which accepts an array of objects and a key, and a value, and returns true if every single object in the array contains that value for the specific key. Otherwise it should return false.

Examples:
    var arr = [
        {title: "Instructor", first: 'Elie', last:"Schoppik"}, 
        {title: "Instructor", first: 'Tim', last:"Garcia", isCatOwner: true}, 
        {title: "Instructor", first: 'Matt', last:"Lane"}, 
        {title: "Instructor", first: 'Colt', last:"Steele", isCatOwner: true}
    ]

    hasCertainValue(arr,'title','Instructor') // true
    hasCertainValue(arr,'first','Elie') // false

*/

function hasCertainValue(arr, key, searchValue){
    return arr.every(function(d){
        return d[key] === searchValue;
    })
}
```

## reduce

### Definition

1.  Accepts a callback function and an optional second parameter
2.  Iterates through an array
3.  Runs a callback on each value in the array
4.  The first parameter to the callback is either the first value in the array
    or the optional second parameter
5.  The first parameter to the callback is often called accumulator
6.  The returned value from the callback becomes the new value of accumulator
7.  Whatever is returned from the callback function, becomes the new value of
    the accumulator

### Anatomy of reduce

```javascript
array.reduce(callback funtion(accumulator, nextValue, index, array){
    // whatever is returned inside here, will be the value of accumulator in the next iteration
}, optional second parameter)
```

#### accumulator: first value in array or optional second parameter

#### nextValue: second value in array or first if optional second parameter is passed

#### index: each index in the array

#### array: the entire array

### Example

#### sum an array, no second parameter

```javascript
var arr = [1,2,3,4,5];

arr.reduce(function(accumulator, nextValue){
    return accumulator + nextValue;
})
```

#### sum an array, with second parameter

```javascript
var arr = [1,2,3,4,5]

arr.reduce(function(accumulator, nextValue){
    return accumulator + nextValue;
}, 10)
```

#### strings

```javascript
var names = ["Tim", "Matt", "Colt", "Elie"];

names.reduce(function(acc,nextValue){
    return acc + " " + nextValue;
}, "The instructors are")
```

#### objects

```javascript
var arr = [5,4,1,4,5,6,7,3,4,4,1]

arr.reduce(function(acc, nextVal){
    if (nextVal in acc) {
        acc[nextVal]++;
    } else {
        acc[nextVal] = 1
    }
    return acc;
}, {})
```

### Use reduce in a function

#### sum Odd Numbers

```javascript
var sumOddNumbers = (arr) => {
    return arr.filter(function(d){
        return d%2 !== 0;
    }).reduce(function(acc,nextVal){
        return acc + nextVal;
    })
}
```

#### create Full Name

```javascript
var createFullName = function(arr){
    return arr.reduce(function(acc,nextVal){
        acc.push(nextVal.first+" "+nextVal.last);
        return acc;
    },[]);
}
```

### Reduce Exercise

```javascript
/*
Write a function called extractValue which accepts an array of objects and a key and returns a new array with the value of each object at the key.

Examples:
    var arr = [{name: 'Elie'}, {name: 'Tim'}, {name: 'Matt'}, {name: 'Colt'}]
    extractValue(arr,'name') // ['Elie', 'Tim', 'Matt', 'Colt']
*/

function extractValue(arr, key){
    return arr.reduce(function(acc, nextVal){
        acc.push(nextVal[key]);
        return acc;
    },[])
}


/*
Write a function called vowelCount which accepts a string and returns an object with the keys as the vowel and the values as the number of times the vowel appears in the string. This function should be case insensitive so a lowercase letter and uppercase letter should count

Examples:
    vowelCount('Elie') // {e:2,i:1};
    vowelCount('Tim') // {i:1};
    vowelCount('Matt') // {a:1})
    vowelCount('hmmm') // {};
    vowelCount('I Am awesome and so are you') // {i: 1, a: 4, e: 3, o: 3, u: 1};
*/

function vowelCount(str){
    return str.split("").reduce(function(acc,nextVal){
        if ("aeiou".includes(nextVal.toLowerCase()) && (nextVal.toLowerCase() in acc)) {
            acc[nextVal.toLowerCase()]++
        } else if ("aeiou".includes(nextVal.toLowerCase())) {
            acc[nextVal.toLowerCase()] = 1
        }
        return acc
    },{})
}

// a:0,e:0,i:0,o:0,u:0
/*
Write a function called addKeyAndValue which accepts an array of objects and returns the array of objects passed to it with each object now including the key and value passed to the function.

Examples:
    var arr = [{name: 'Elie'}, {name: 'Tim'}, {name: 'Matt'}, {name: 'Colt'}];

    addKeyAndValue(arr, 'title', 'Instructor') // 
      [
        {title: 'Instructor', name: 'Elie'}, 
        {title: 'Instructor', name: 'Tim'}, 
        {title: 'Instructor', name: 'Matt'}, 
        {title: 'Instructor', name: 'Colt'}
       ]
*/

function addKeyAndValue(arr, key, value){
    return arr.reduce(function(acc, nextVal,i,array){
        acc[i][key] = value;
        return acc;
    },arr)
}


/*
Write a function called partition which accepts an array and a callback and returns an array with two arrays inside of it. The partition function should run the callback function on each value in the array and if the result of the callback function at that specific value is true, the value should be placed in the first subarray. If the result of the callback function at that specific value is false, the value should be placed in the second subarray. 

Examples:

    function isEven(val){
        return val % 2 === 0;
    }

    var arr = [1,2,3,4,5,6,7,8];

    partition(arr, isEven) // [[2,4,6,8], [1,3,5,7]];

    function isLongerThanThreeCharacters(val){
        return val.length > 3;
    }

    var names = ['Elie', 'Colt', 'Tim', 'Matt'];

    partition(names, isLongerThanThreeCharacters) // [['Elie', 'Colt', 'Matt'], ['Tim']]
*/

function partition(arr, callback){
    return arr.reduce(function(acc,nextVal,i,array){
        if (callback(nextVal)) {
            acc[0].push(nextVal);
        } else {
            acc[1].push(nextVal);
        }
        return acc;
    },[[],[]])
}
```

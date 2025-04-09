// challenge 1
console.log(capitalize("alice"));

function capitalize(str){
  return str.charAt(0).toUpperCase() + str.slice(1);
};

// challenge 2
function capitalizeSentence(sentence) {
    return sentence.split(" ").map(word => capitalize(word)).join(" ");
}
console.log(capitalizeSentence("alice"));
console.log(capitalizeSentence("alice in wonderland"));

// challenge 3

const ids = new Set();
const generateId = () => {
  let id = 0;
  do {
    id++;
  } while (ids.has(id));

  ids.add(id);
  return id;
};

//old implementation:
// const ids = [];
// const generateId = () => {
//   let id = 0;
//   do {
//     id++;
//   } while (ids.includes(id));

//   ids.puh(id);
//   return id;
// };

console.time("generateId"); //mesure time
for (let i = 0; i < 3000; i++) {
  generateId();
}
console.timeEnd("generateId");

// challenge 4
function compareObjects(obj1, obj2) {
    if (typeof obj1 !== 'object' || obj1 === null ||
        typeof obj2 !== 'object' || obj2 === null) {
      return obj1 === obj2;
    }
    const keys1 = Object.keys(obj1);
    const keys2 = Object.keys(obj2);
    if (keys1.length !== keys2.length) return false;
  
    for (let key of keys1) {
      if (!keys2.includes(key) || !compareObjects(obj1[key], obj2[key])) {
        return false;
      }
    }
    return true;
}

const obj1 = {
    name: "Alice",
    age: 25,
    address: {
      city: "Wonderland",
      country: "Fantasy",
    },
};
  
const obj2 = {
  name: "Alice",
  age: 25,
  address: {
    city: "Wonderland",
    country: "Fantasy",
  },
};

const obj3 = {
  age: 25,
  address: {
    city: "Wonderland",
    country: "Fantasy",
  },
  name: "Alice",
};

const obj4 = {
  name: "Alice",
  age: 25,
  address: {
    city: "Not Wonderland",
    country: "Fantasy",
  },
};

const obj5 = {
  name: "Alice",
};
  
console.log("Should be True:", compareObjects(obj1, obj2));
console.log("Should be True:", compareObjects(obj1, obj3));
console.log("Should be False:", compareObjects(obj1, obj4));
console.log("Should be True:", compareObjects(obj2, obj3));
console.log("Should be False:", compareObjects(obj2, obj4));
console.log("Should be False:", compareObjects(obj3, obj4));
console.log("Should be False:", compareObjects(obj1, obj5));
console.log("Should be False:", compareObjects(obj5, obj1));

// challenge 5
let library = [];

const addBookToLibrary = (title, author, pages, isAvailable, ratings) => {
  if (typeof title !== 'string' || title.trim() === '') {
    throw new Error('Title must be a not empty string.');
  }
  if (typeof author !== 'string' || author.trim() === '') {
    throw new Error('Author must be a not empty string.');
  }
  if (typeof pages !== 'number' || pages <= 0 || !Number.isInteger(pages)) {
    throw new Error('Pages must be a positive number.');
  }
  if (typeof isAvailable !== 'boolean') {
    throw new Error('isAvailable must be a boolean.');
  }
  if (!Array.isArray(ratings)) {
    throw new Error('Ratings must be an array.');
  }
  for (const rating of ratings) {
    if (typeof rating !== 'number' || rating < 0 || rating > 5) {
      throw new Error('Each rating must be a number between 0 and 5.');
    }
  }

  library.push({
    title: title.trim(),
    author: author.trim(),
    pages,
    available: isAvailable,
    ratings,
  });
};

// challenge 6
const testAddingBooks = (testCases) => {
  testCases.forEach(({ testCase, shouldFail }, index) => {
    try {
      addBookToLibrary(...testCase);
      if (shouldFail) {
        console.log(`Test ${index + 1} failed`);
        console.log('Test case:', testCase);
      } else {
        console.log(`Test ${index + 1} passed`);
        console.log('Test case:', testCase);
      }
    } catch (error) {
      if (shouldFail) {
        console.log(`Test ${index + 1} passed`);
        console.log('Test case:', testCase);
        console.log('Error message:', error.message);
      } else {
        console.log(`Test ${index + 1} failed`);
        console.log('Test case:', testCase);
        console.log('Error message:', error.message);
      }
    }
    console.log();
  });
};


const testCases = [
  { testCase: ["", "Author", 200, true, []], shouldFail: true },
  { testCase: ["Title", "", 200, true, []], shouldFail: true },
  { testCase: ["Title", "Author", -1, true, []], shouldFail: true },
  { testCase: ["Title", "Author", 200, "yes", []], shouldFail: true },
  { testCase: ["Title", "Author", 200, true, [1, 2, 3, 6]], shouldFail: true },
  {
    testCase: ["Title", "Author", 200, true, [1, 2, 3, "yes"]],
    shouldFail: true,
  },
  { testCase: ["Title", "Author", 200, true, [1, 2, 3, {}]], shouldFail: true },
  { testCase: ["Title", "Author", 200, true, []], shouldFail: false },
  { testCase: ["Title", "Author", 200, true, [1, 2, 3]], shouldFail: false },
  { testCase: ["Title", "Author", 200, true, [1, 2, 3, 4]], shouldFail: false },
  {
    testCase: ["Title", "Author", 200, true, [1, 2, 3, 4, 5]],
    shouldFail: false,
  },
  {
    testCase: ["Title", "Author", 200, true, [1, 2, 3, 4, 5]],
    shouldFail: false,
  },
];

testAddingBooks(testCases);

// challenge 7
const addBooksToLibrary = (books) => {
  books.forEach(book => {
    try {
      addBookToLibrary(...book);
    } catch (error) {
      console.error(`Error while adding a book!`, error);
    }
  });
};

const books = [
  ["Alice in Wonderland", "Lewis Carroll", 200, true, [1, 2, 3]],
  ["1984", "George Orwell", 300, true, [4, 5]],
  ["The Great Gatsby", "F. Scott Fitzgerald", 150, true, [3, 4]],
  ["To Kill a Mockingbird", "Harper Lee", 250, true, [2, 3]],
  ["The Catcher in the Rye", "J.D. Salinger", 200, true, [1, 2]],
  ["The Hobbit", "J.R.R. Tolkien", 300, true, [4, 5]],
  ["Fahrenheit 451", "Ray Bradbury", 200, true, [3, 4]],
  ["Brave New World", "Aldous Huxley", 250, true, [2, 3]],
  ["The Alchemist", "Paulo Coelho", 200, true, [1, 2]],
  ["The Picture of Dorian Gray", "Oscar Wilde", 300, true, [4, 5]],
];

addBooksToLibrary(books);
console.log(library);  
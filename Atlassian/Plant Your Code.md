## // LEVEL 1.1

Plant your seeds. Because a square grid is the best layout for these and future seeds, write a function that determines the most efficient layout.

```js
/**
 * Determines how many rows and columns your garden will
 * need to be closest to a square given a number of seeds.
 *
 * @param {number} seedCount - The number of seeds in your
 * seed packet.
 * @return {array} - [rows, columns] needed for your grid
 * layout (for example [4, 5] represents a 4 row x 5 column
 * grid)
*/
  
function grid(seedCount) {
    let minAxis = Math.round(Math.sqrt(seedCount))
    let otherAxis = Math.round(seedCount / minAxis)
    return [minAxis, otherAxis]
}
```

## // LEVEL 1.2

Make sure your plants are thriving. The more sun they get, the more water they need. Write a function that locates plants in your garden that need water.

```js
/**
 * The following represents all your plants' locations 
 * in your garden and whether they need water.
 * 
 * const plant_1 = {
 *      gardenLocation: [1, 1],
 *      needsWater: true
 * };
 * 
 * const plant_2 = {
 *      gardenLocation: [1, 2],
 *      needsWater: false
 * };
 * 
 * const plant_3 = {
 *      gardenLocation: [2, 1],
 *      needsWater: false
 * };
 * 
 * const plant_4 = {
 *      gardenLocation: [2, 2],
 *      needsWater: true
 * };
 * 
 * const plants = [plant_1, plant_2, plant_3, plant_4];
*/

/**
 * Write a function that takes in your array of plants and 
 * returns a new array of garden locations you should water.
 *
 * @param {array} plants - Your array of plants.
 * @return {array} - An array of garden locations you should 
 * water.
 */

function whereToWater(plantsArray) {
    plantsToWater = []
    for (let plant of plantsArray) {
        if (plant.needsWater) plantsToWater.push(plant.gardenLocation)
    }
    return plantsToWater
}
```

## // LEVEL 1.3

Give your plants CO2 by talking to them. Complete the following function that converts any string into Plant-Latin so that your plants can understand you.

NOTES: Plant-Latin has different vowels than we do. Append "tiva" after every vowel "a", "llia" after every vowel "e", "mus" after every vowel "i", "phylum" after every vowel "o", and "rea" after every vowel "u". For example: "I love water!" becomes "Imus lophylumvellia wativatelliar!"

```js
/**
 * Converts a message into Plant-Latin.
 * @param {string} message - The message to be translated in lowercase.
 * @return {string} - Translated Plant-Latin message.
 */
  
function translatePlantLatin(message) {
    let output = ''
    lower = message.toLowerCase()
    for (let char of lower) {
        switch (char) {
            case 'a':
                output += char + 'tiva'
                break
            case 'e':
                output += char + 'llia'
                break
            case 'i':
                output += char + 'mus'
                break
            case 'o':
                output += char + 'phylum'
                break
            case 'u':
                output += char + 'rea'
                break
            default:
                output += char
                break
        }
    }
    return output
}
```

## // LEVEL 2.1

Plant your new seeds. This time, write a function that takes an array of seeds and any number of rows and columns to plant your seeds in a grid represented by a 2D array.

```js
/**
 * Returns a 2D array representing all seeds in a grid of size 
 * row x cols.
 *
 * @param {array} seeds - Array of the Seeds in your packet.
 * @param {number} rows - The number of rows.
 * @param {number} cols = The number of columns.
 * @return {array} - 2D array representing grid of planted Seeds.
 */
  
function grid(seeds, rows, cols) {
    let count = 0
    let out = []
    for (let i = 0; i < rows; i++) {
        out.push([])
        for (let j = 0; j < cols; j++) {
            out[i].push(seeds[count++])
        }
    }
    return out
}
```

## // LEVEL 2.2

A plant needs help. Using the same rules of Plant-Latin as before, write a function that sorts through the array of plants and returns the one calling out for "help".

```js
/**
 * Converts a message from Plant-Latin.
 * @param {string} message - The Plant-Latin message to be translated.
 * @return {string} - Translated message.
 */

function translate(message) {
    const vowelReplacements = {
        tiva: "a",
        llia: "e",
        mus: "i",
        phylum: "o",
        rea: "u"
    };
    let newMessage = message.toLowerCase();
    for (const vowel in vowelReplacements) {
        newMessage = newMessage.split(vowel).join('')
    }
    return newMessage
}

/**
* The Plant class has an instance property called message
* which is a string. The Plant's message is in Plant-Latin.
* Write a function that takes in an array of Plants, a message
* in human language, and returns all the Plants whose Plant-Latin
* matches the message.
*
* @param {array} plants - Array of Plants to be searched
* @param {string} message - The message in human language to search for
* @return {array} - Array of Plants whose Plant-Latin translates to message
*/

function searchPlantsForMessage(plants, message) {
    let output = []
    plants.forEach(p => {if (translate(p.message) == message) output.push(p)});
    return output
}
```

## // LEVEL 2.3

Some plants need more sun. Write a function that re-orders your plants so that their heights don't cast shadows on each other and then prioritizes your plants by their health.

```js
/**
 * The Plant class
 */

var Plant = class Plant {
/**
 * @param {number} height - height in number of inches
 * @param {string} health - string of either "below average", "average", or
 * "above average"
 */
  constructor(height, health) {
    this.height = height;
    this.health = health;
  }
}

/**
 *
 * Write a function that passes in an array of Plants and
 * orders the array from shortest Plant to tallest.
 * If two heights are the same, then order by least healthiest
 * to healthiest.
 *
 * @param {Plant[]} plants - Array of Plants
 * @return {array} - Array of Plants ordered from shortest
 * to tallest.
 */

function reorderPlants(plants) {
    const h = ["below average","average","above average"];
    let answer = plants.sort((a,b) => {
        if (a.height < b.height)
            return -1;
        else if (a.height > b.height)
            return 1;
        else{
            if (h.indexOf(a.health) < h.indexOf(b.health))
                return -1
            else if (h.indexOf(a.health) > h.indexOf(b.health))
                return 1
            else
                return 0;
        }
    });
    return answer;
}
```

## // LEVEL 3.1

Your new seeds come with very specific instructions. "Please plant me in soil that grew KALE last season." You’ll need to connect to an API and get last season’s growing records and then determine which sections of soil your new seeds will thrive in.

```js
/**
 * Determine the locations in your garden layout where a given
 * plant was planted last year based on API data. The garden layout
 * is represented as a 2D array of Plants. Plants are represented
 * as strings by their name.
 *
 * Complete the following function that takes a plant's name,
 * garden layout API endpoint data that retrieves a 2D array of plant names,
 * and returns an array of that plant's locations {row: number, col: number}
 * from last year's garden layout.
 *
 * @param {string} plantName - The name of plant to find in garden layout
 * @param {string} endpointUrl -accept a URL endpoint to retrieve data from.
 *        Will return JSON similar to this example endpoint:
 *        https://https://plantyourcode.com/api/previous-locations
 * @return {array} - Array of locations {row: number, col: number} for each location
*/
async function findPlantLocations(plantName, endpointUrl) {
    let data
    await fetch(endpointUrl)
        .then((response) => response.json())
        .then((jsonData) => {
            data = jsonData["garden-2019"]
        });
    
    data = data.substring(2, data.length-2)
    data = data.replace(/[/']/g, "")
    data = data.replace(/[/ ]/g, "")
    data = data.split("],[")
    
    let arr = [];
    for(let i = 0; i < data.length; i++) {
        arr[i] = data[i].split(',')
    }
    console.log(arr)

    let answer = [];
    for(let i = 0; i < arr.length; i++) {
        for(let j = 0; j < arr[i].length; j++) {
            if (arr[i][j] == plantName) {
                answer.push({row: i, col: j})
            }
        }
    }

    return(answer)
}
```

`api/previous-locations`

```json
{"garden-2019":"[['tomato', 'tomato', 'cucumber'],['tomato', 'tomato', 'cucumber'],['green-peppers', 'green-peppers', 'cucumber'],['red-peppers', 'red-peppers', 'cucumber'],['cilantro', 'kale', 'kale'],['cilantro', 'kale', 'kale']]"}
```

## // LEVEL 3.2

Your plants are getting hungry! Each requires a different set of nutrients—luckily you’ve logged this data in your journal. Create a class called CustomPlantFood that extends the base plant food class, and then write a function that determines how much food each plant needs.

```js
/**
  * Below is an example of the input plantData. Actual values may vary.
  *
  * {
  *  "tomato": {
  *    "nutrients-required": ['nitrogen', 'calcium', 'magnesium'],
  *    "grams-food-per-plant": 3, // amount of plant food needed in grams per plant
  *    "current-count": 6 // amount of plants currently in your garden
  *  },
  *    "blueberries": {
  *    "nutrients-required": ['nitrogen', 'phosphorus', 'potassium', 'sulfur', 'boron'],
  *    "grams-food-per-plant": 2,
  *    "current-count": 4
  *  },
  *    "chard": {
  *    "nutrients-required": ['phosphorus', 'potassium', 'calcium', 'magnesium', 'cobalt', 'iron'],
  *    "grams-food-per-plant": 2,
  *    "current-count": 8
  *  }
  * }
  */

  var BasePlantFood = class BasePlantFood {
    constructor() {
        this.nutrients = ["nitrogen", "phosphorus", "potassium", "calcium"];
    }

    getAmountNeeded(count, grams) {
        return count * grams;
    }
  }

  /**
   * Create a class CustomPlantFood that extends the BasePlantFood class.
   * It should initialize with its additional nutrients required.
  */

  var CustomPlantFood = class CustomPlantFood extends BasePlantFood {
    constructor(plant) {
        super();
        this.grams = plant["grams-food-per-plant"];
        this.count = plant["current-count"];
        this.addNutrients(plant["nutrients-required"]);
    }

    /**
     * Write a function that adds nutrients to the base plant food.
     * Any nutrients already included in the base plant food should
     * not be added twice.
     *
     * @param {array} nutrients - array of strings of nutrient names
    */

    addNutrients(nutrients) {
        nutrients.forEach((nutrient) => {
            if (!this.nutrients.includes(nutrient)) {
                this.nutrients.push(nutrient);
            }
        });
    }
  }

  /**
   *
   * Write a function that determines the amount of each custom
   * plant food you'll need based off the provided plantData object.
   * For each type of plant food, create a new instance of the
   * CustomPlantFood class.
   *
   * @return {array} - Array of objects {food: CustomPlantFood, gramsNeeded: number}
  */

  function determineCustomPlantFoods(plantData) {
    const nutrients = [];

    for (plant of Object.keys(plantData)) {
        console.log(plant);
        let n = new CustomPlantFood(plantData[plant]);
        nutrients.push({ food: n, gramsNeeded: n.getAmountNeeded(n.count, n.grams)});
    }

    return nutrients;
  }
```

## // LEVEL 3.3

Start tracking your new plant conversations. In previous years, your journal entries have been formatted: `row-col type: message [number of times spoken].`

For example: `3-2 tomato: hungry i am [43]`

Now, you'd rather see the number of times spoken come first, followed by the type: message and row-col. Complete the following function that restructures your communication log.

```js
/**
 * You've been recording logs of your plants speaking in
 * the following format grid location, message, count.
 * Write a function that takes in a string from your log
 * and properly rearranges so that the count is first,
 * followed by the message, then the grid location.
 *
 * @param {string} log - A string of a log in your journal
 * @return {string} - New rearranged string
*/
  
function rearrangeLog(log) {
    const re = new RegExp(/^(\d+)-(\d+) (\S+): (.*) \[(\d+)\]$/);
    const groups = re.exec(log);
    return `[${groups[5]}] ${groups[3]}: ${groups[4]} ${groups[1]}-${groups[2]}`;
}
```

## // LEVEL 4.1

Some of your plants' roots are starting to rot. You’ve studied the root system and sketched out what you see. This type of fungus infects your roots at each node. Write a function that will return your new root system after you've pruned all unhealthy nodes that don’t have healthy nodes below it.

```js
/**
 * We have a root structure in the form of a binary tree where
 * a value of 0 is unhealthy and 1 is healthy. A null value
 * indicates that the node position is empty. A subtree of a
 * node n is n, plus every node that is a descendant of n.
 *
 *
 *  Definition for a binary tree node.
 *  @param {integer} data - 0 or 1
 *  @param {Node} left - subtree or null for no left branch
 *  @param {Node} right - subtree or null for no right branch
 *  function Node(data, left, right) {
 *      this.data = data === undefined ? 0 : data;
 *      this.left = left === undefined ? null : left;
 *      this.right = right === undefined ? null : right;
 *  }
 *
 * Complete the following that determines which nodes to prune in
 * order to prune all unhealthy nodes that don't have healthy nodes
 * as children and return the result. Set pruned nodes to null.
 *
 * @param {Node} root - binary tree data representing the root system of the plant
 * @return {Node} - binary tree data representing the pruned root system of the plant
 */
function pruneRoots(root) {
    if (root === null) {
        return root;
    }

    if (root.data === 0 && !hasHealthyChild(root)) {
        root = null;
    } else {
        root.left = pruneRoots(root.left);
        root.right = pruneRoots(root.right);
    }

    return root;
}

function hasHealthyChild(root) {
    if (root === null) {
        return false;
    }

    if (root.left?.data === 1 || root.right?.data === 1) {
        return true;
    } else {
        return hasHealthyChild(root.left) || hasHealthyChild(root.right);
    }
}
```

## // LEVEL 4.2

A row of your plants is infested with bugs! Each day, plants with more infestation than the plant to their left will die. Write a function to find out how many days it will take for the infestation to end.

For example: If infestation levels for each plant in the row are `[3, 7, 2, 9, 1, 6, 4]` then, on the first day, plants infested at levels 7, 9, and 6 will die leaving `[3, 2, 1, 4]`. On the second day 4 will die leaving `[3, 2, 1]` with no more plants that will die. The answer is 2 days.

```js
/**
* Complete the function plantsDying below. It must return
* the number of days until plants will no longer die from infestation. 
* If a plant has a higher infestation number than the plant to it's left, it dies.
*
* @param {array} infestedPlants - Array of the infestation levels of the row of plants
* @return {number} - Number representing the number of days until plants no longer die
*/

function plantsDying(infestedPlants) {
  let cur = [...infestedPlants];
    let days = 0;

    while (infested(cur)) {
        days++;
        cur = clean(cur);
    }

    return days;
}

function infested(plants) {
    for (let i = 0; i < plants.length - 1; i++) {
        if (plants[i + 1] > plants[i]) {
            return true;
        }
    }

    return false;
}

function clean(infestedPlants) {
    let toRemove = [];

    for (let i = 0; i < infestedPlants.length - 1; i++) {
        if (infestedPlants[i + 1] > infestedPlants[i]) {
            toRemove.push(i + 1);
        }
    }

    let uninfestedPlants = [];

    for (let i = 0; i < infestedPlants.length; i++) {
        if (!toRemove.includes(i)) {
            uninfestedPlants.push(infestedPlants[i]);
        }
    }

    return uninfestedPlants;
}
```

## // LEVEL 4.3

Someone wants to buy your plants! The catch is, the buyer only wants the largest region of mINT in your garden, which is mixed in a uniform grid with CHARd. Figure out how many plants the buyer will buy.

A region is a group of contiguously adjacent plants of a single type. Plants are considered adjacent if they are next to each other horizontally, vertically, or diagonally.

For example: if you have the following garden where m is mINT and c is CHARd you will sell the buyer 5 mINT plants.

`m m c c m`
`c m m c m`
`c c m c c`
`m c c c m`
`c c c m m`

```js
/**
* Find and return the single largest region of mINT plants in a 2D array representing 
* a garden plot. The function can accept any size of 2D array and solves for 
* a value of "m" when finding mINT plants.
* 
* @param {array} garden - 2D array of a mixed garden where m is mINT and c is CHARd
* @return {number} - Number representing the largest region of mINT plants
*/

function findBiggestRegion(garden) {
    let dx = [1, 1, 0, -1, -1, 0, 1];
    let dy = [0, 1, 1, 1, 0, -1, -1, -1];
    let vis = {};
    let totalM = 0;
    let max = 0;
    for (let i = 0; i < garden.length; i++) {
        vis[i] = {};
    }

    function check(x, y) {
        return x >= 0 && x < garden.length && y >= 0 && y < garden[0].length;
    }

    function dfs(i, j) {
        totalM++;
        vis[i][j] = true;

        for (let k = 0; k < 8; k++) {
            let x = i + dx[k];
            let y = j + dy[k];

            if (check(x, y) && vis[x][y] !== true && garden[x][y] === "m") {
                dfs(x, y);
            }
        }
    }

    for (let i = 0; i < garden.length; i++) {
        for (let j = 0; j < garden[0].length; j++) {
            totalM = 0;

            if (garden[i][j] === "m") {
                dfs(i, j);
            }

            if (totalM > max) {
                max = totalM;
            }
        }
    }

    return max;
}
```

## // BONUS LEVEL

A severe cold snap is coming. You need to pot your plants and get them inside ASAP.

You can produce n potted plants per day at a rate of `shovels x helpers`. While there is no limit on the number of garden shovels you own or helpers employed, to have either will cost you your plants. Each day, you can sell some of your newly potted plants to buy more garden shovels or hire more helpers.

Determine the least number of days it takes to save your plants.

For example: if your house has room for 70 plants, you start with 1 garden shovel and 2 helpers, and it costs 2 plants to buy a garden shovel or hire another helper, it will take 5 days to save the 70 plants.

```js
/**
* Complete the function daysToSavePlants below. It should return the least number of
* days possible to save a fixed number of potted plants when starting with a certain
* number of garden shovels and helpers which can be increased by spending some of the
* produced potted plants.
*
* @param {number} plantsToSave - Target number of potted plants to bring inside
* @param {number} shovels - Starting amount of shovels
* @param {number} helpers - Starting number of helpers
* @param {number} plantsToBuyResources - Number of rescued plants it costs to by a shovel or employ a helper
* @return {number} - The least number of days to save the target number of plants 
*/
function daysToSavePlants(
  plantsToSave,
  shovels,
  helpers,
  plantsToBuyResources
) {
    
}
```
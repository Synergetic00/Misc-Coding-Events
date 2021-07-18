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
```

# Dump of Solutions (WIP)

Level 2.3

function reorderPlants(plants) {
    /* Enter your solution here! */
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
    /* your code here */
    });
    return answer;
}


Level 3.1

async function findPlantLocations(plantName, endpointUrl) {
    /* Enter your solution here! */
    let data
    await fetch(endpointUrl)
        .then((response) => response.json())
        .then((jsonData) => {
            data = jsonData["garden-2019"]
        });
        
    data = data.substring(2,data.length-2)
    data = data.replace(/[/']/g,"")
    data = data.replace(/[/ ]/g,"")
    data = data.split("],[")
    
    let arr = [];
    for(let i = 0; i < data.length; i++){
        arr[i] = data[i].split(',')
    }
    console.log(arr)

    let answer = [];
    for(let i = 0; i < arr.length; i++){
        for(let j = 0; j < arr[i].length; j++){
            if (arr[i][j] == plantName){
                answer.push({row: i, col: j})
            }
        }
    }

    return(answer)

}

// Level 3.2

var BasePlantFood = class BasePlantFood {
    constructor() {
        this.nutrients = ["nitrogen", "phosphorus", "potassium", "calcium"];
    }

    getAmountNeeded(count, grams) {
        return count * grams;
    }
};

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
        /* Enter your solution here! */
        nutrients.forEach((nutrient) => {
            if (!this.nutrients.includes(nutrient)) {
                this.nutrients.push(nutrient);
            }
        });
    }
};

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
    /* Enter your solution here! */

    const nutrients = [];

    for (plant of Object.keys(plantData)) {
        console.log(plant);
        let n = new CustomPlantFood(plantData[plant]);

        nutrients.push({
            food: n,
            gramsNeeded: n.getAmountNeeded(n.count, n.grams),
        });
    }

    return nutrients;
}

// Level 3.3

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
    /* Enter your solution here! */
    const re = new RegExp(/^(\d+)-(\d+) (\S+): (.*) \[(\d+)\]$/);

    const groups = re.exec(log);

    return `[${groups[5]}] ${groups[3]}: ${groups[4]} ${groups[1]}-${groups[2]}`;
}

// Level 4.1

class Node {
    constructor(data, left, right) {
        this.data = data === undefined ? 0 : data;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
    }
}

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
    /* Enter your solution here! */
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

// Level 4.2

/**
 * Complete the function plantsDying below. It must return
 * the number of days until plants will no longer die from infestation.
 * If a plant has a higher infestation number than the plant to it's left, it dies.
 *
 * @param {array} infestedPlants - Array of the infestation levels of the row of plants
 * @return {number} - Number representing the number of days until plants no longer die
 */

function plantsDying(infestedPlants) {
    /* Enter your solution here! */
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

// Level 4.3

/**
 * Find and return the single largest region of mINT plants in a 2D array representing
 * a garden plot. The function can accept any size of 2D array and solves for
 * a value of "m" when finding mINT plants.
 *
 * @param {array} garden - 2D array of a mixed garden where m is mINT and c is CHARd
 * @return {number} - Number representing the largest region of mINT plants
 */

function findBiggestRegion(garden) {
    /* Enter your solution here! */
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
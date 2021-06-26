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


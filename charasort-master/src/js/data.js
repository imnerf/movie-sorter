/**
 * @typedef {{name: string, key: string, tooltip?: string, checked?: boolean, sub?: {name: string, tooltip?: string, checked?: string}[]}[]} Options
 * @typedef {{name: string, img: string, opts: Object<string, boolean|number[]}[]} CharData
*/

/**
 * Data set. Characters will be removed from the sorting array based on selected options, working down the array.
 * 
 * @type {Object.<string, {options: Options, characterData: CharData}>}
*/
const dataSet = {};

/** 
 * Data set version, in YYYY-MM-DD form.
 * 
 * @example '2024-10-18'
*/
let dataSetVersion = '2024-10-18';

/**
 * Image root, will be appended to the start of every image URL.
 */
const imageRoot = ''; // Leave this empty since you're not using images right now

/**
 * Data set. Movies will be removed from the sorting array based on selected options, working down the array.
 * 
 * @type {Object.<string, {options: Options, characterData: CharData}>}
 */

// Load the dataset for the movie sorter
dataSet[dataSetVersion] = {};
dataSet[dataSetVersion].options = [
  // Optional: Add your filtering options here later
];

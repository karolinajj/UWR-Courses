/**
 * @typedef {Object} Product
 * @property {number} id - Product id
 * @property {string} name - Product name
 * @property {number} quantity - Number of items to purchase
 * @property {Date} purchaseBy - Date by which the product should be purchased
 * @property {boolean} purchased - Status indicating whether the product has been purchased
 * @property {number} [pricePerUnit] - Optional price per unit (only for purchased products)
 */

/**
 * List of products
 * @type {Product[]}
 */
const productList = [];

/**
 * Adds a new product to the list
 * @param {string} name - Product name
 * @param {number} quantity - Number of items to purchase
 * @param {string} purchaseByString - Date as a string (YYYY-MM-DD)
 * @param {boolean} purchased - Status indicating whether the product has been purchased
 * @param {number} [pricePerUnit] - Optional price per unit (only for purchased products)
 */
function add_to_products(name, quantity, purchaseByString, purchased, pricePerUnit=undefined) {
    const newProduct = {
        id: Math.floor(Math.random() * 1000000),
        name,
        quantity,
        purchaseBy: new Date(purchaseByString),
        purchased,
        pricePerUnit: purchased ? pricePerUnit : undefined
    };
    productList.push(newProduct);
}

/**
 * Removes a product from the list by id
 * @param {number} id - Product id to remove
 */
function remove_product(id) {
    const index = productList.findIndex(product => product.id === id);
    if (index !== -1) {
        productList.splice(index, 1);
    }
}

/**
* Updates the name of a product by id
* @param {number} id - Product id
* @param {string} newName - New product name
*/
function update_product_name(id, newName) {
    const product = productList.find(product => product.id === id);
    if (product) {
        product.name = newName;
    }
}

/**
* Updates the quantity of a product by id
* @param {number} id - Product id
* @param {number} newQuantity - New quantity value
*/
function update_product_quantity(id, newQuantity) {
    const product = productList.find(product => product.id === id);
    if (product) {
        product.quantity = newQuantity;
    }
}

/**
* Updates the purchase date of a product by id
* @param {number} id - Product id
* @param {string} newPurchaseByString - New purchase date as a string (YYYY-MM-DD)
*/
function update_product_purchase_date(id, newPurchaseByString) {
    const product = productList.find(product => product.id === id);
    if (product) {
        product.purchaseBy = new Date(newPurchaseByString);
    }
}

/**
* Updates the purchase status of a product by id
* @param {number} id - Product id
* @param {boolean} newStatus - New purchase status
*/
function update_product_status(id, newStatus) {
    const product = productList.find(product => product.id === id);
    if (product) {
        product.purchased = newStatus;
    }
}
/**
 * Moves a product to a new position in the list, shifting the positions of other elements.
 * @param {number} idx - Index of the product to move in the productList (not product.id)
 * @param {number} newIdx - New index position in the list
 */
function move_product(idx, newIdx) {
    if (newIdx < 0 || newIdx >= productList.length || idx === newIdx) {
        return;
    }

    const [product] = productList.splice(idx, 1);

    if (newIdx > idx) {
        productList.splice(newIdx, 0, product);
    } else {
        productList.splice(newIdx, 0, product);
    }
}

/**
 * Gets products that should be purchased today
 * @returns {Product[]} List of products due today
 */
function products_today() {
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    return productList.filter(product => {
        const productDate = new Date(product.purchaseBy);
        productDate.setHours(0, 0, 0, 0);

        return !product.purchased && productDate.getTime() === today.getTime();
    });
}

/**
 * Sets the price per unit for a purchased product.
 * If the product is not marked as purchased, the function does nothing.
 * @param {number} id - Product id
 * @param {number} price - Price per unit
 */
function set_product_price(id, price) {
    const product = productList.find(product => product.id === id);
    if (product && product.purchased) {
        product.pricePerUnit = price;
    }
}

/**
 * Calculates the cost of bought products with the expiration date.
 * @param {string} date - Product id
 */
function cost_by_date(date) {
    res = 0;
    const dateNormalized = new Date(date);
    dateNormalized.setHours(0, 0, 0, 0);

    for (let i = 0; i < productList.length; i++) { 
        const productDate = new Date(productList[i].purchaseBy);
        productDate.setHours(0, 0, 0, 0);

        if(productList[i].purchased && productDate.getTime() === dateNormalized.getTime() && productList[i].pricePerUnit !== undefined){
            res += productList[i].pricePerUnit;
        }
    }
    return res;

}

/**
 * Modifies products based on provided IDs and a modification function.
 * @param {number[]} indexes - Array of product IDs to modify
 * @param {Function} modifyFunction - function to modify each product that takes a single product.
 */
function modify_products(indexes, modifyFunction) {
    productList.forEach((product, index) => {
        if (indexes.includes(product.id)) {
            productList[index] = { ...product, ...modifyFunction(product) };
        }
    });
}


add_to_products("a", 2, "2023-12-01", 0);
add_to_products("b", 3, "2023-11-09", 1,2.01);
add_to_products("c", 100, "2023-12-01", 1, 11.99);
add_to_products("d", 90, Date.now(), 0);
add_to_products("e", 11, Date.now(), 0);
add_to_products("f", 1, Date.now(), 1, 2.99);
remove_product(productList[3].id);
console.log("Length ater deletion: ", productList.length);

update_product_name(productList[0].id, "a1")
update_product_quantity(productList[0].id, 7)
update_product_purchase_date(productList[0].id, "2023-11-10")
update_product_status(productList[0].id, 1)
console.log("Updated product: ", productList[0]);

move_product(0,2);
console.log(productList);
move_product(2,0);
console.log(productList);

console.log("Products today:", products_today());

set_product_price(productList[0].id, 7.77)
console.log("Set product price: ", productList[0].pricePerUnit)

set_product_price(productList[3].id, 7.77)
console.log("Set product price: ", productList[3].pricePerUnit)

console.log("Cost by date: ", cost_by_date("2023-12-01"))

modify_products([productList[0].id, productList[3].id],  product => ({ name: product.name + ' New' }));
console.log(productList[0], productList[3]);





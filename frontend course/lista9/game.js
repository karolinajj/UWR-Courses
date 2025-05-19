"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var Endpoints;
(function (Endpoints) {
    Endpoints["ELIXIRS"] = "Elixirs";
    Endpoints["SPELLS"] = "Spells";
})(Endpoints || (Endpoints = {}));
;
let elixirs = [];
let spells = [];
let validOption = undefined;
const gameContainer = document.getElementById("game");
function fetchData(endpoint) {
    return __awaiter(this, void 0, void 0, function* () {
        const response = yield fetch(`https://wizard-world-api.herokuapp.com/${endpoint}`);
        if (!response.ok) {
            throw new Error(`Error fetching data from ${endpoint}`);
        }
        const data = yield response.json();
        return data;
    });
}
//test for fecthData:
//fetchData(Endpoints.SPELLS); //should work
//fetchData("test"); //should not work
//fetchData("Spells"); //should not work
function fetchAllData() {
    return __awaiter(this, void 0, void 0, function* () {
        const [elixirsResponseRaw, spellsResponseRaw] = yield Promise.all([
            fetchData(Endpoints.ELIXIRS),
            fetchData(Endpoints.SPELLS),
        ]);
        const elixirsResponse = elixirsResponseRaw;
        const spellsResponse = spellsResponseRaw;
        elixirs = elixirsResponse.filter((elixir) => elixir.effect);
        spells = spellsResponse.filter((spell) => spell.incantation);
    });
}
function getRandomElements(array, count) {
    const indexes = new Set();
    while (indexes.size < count) {
        const randomIndex = Math.floor(Math.random() * array.length);
        indexes.add(randomIndex);
    }
    return Array.from(indexes).map((index) => array[index]);
}
function generateOptions(randomElements) {
    const [rightOption, ...rest] = randomElements;
    const options = [rightOption, ...rest].sort(() => Math.random() > 0.5 ? 1 : -1);
    return {
        rightOption,
        options,
    };
}
function elixirGame() {
    const { options, rightOption } = generateOptions(getRandomElements(elixirs, 3));
    validOption = rightOption.name;
    console.log(`Cheat Mode: Right answer is ${validOption}`);
    renderOptions(`Which elixir effect is: "${rightOption.effect}"?`, options.map((elixir) => elixir.name));
}
function spellGame() {
    const { options, rightOption } = generateOptions(getRandomElements(spells, 3));
    validOption = rightOption.name;
    console.log(`Cheat Mode: Right answer is ${validOption}`);
    renderOptions(`Which spell incantation is: "${rightOption.incantation}"?`, options.map((spell) => spell.name));
}
function renderOptions(question, answers) {
    const questionElement = document.getElementById("question");
    if (!gameContainer || !questionElement) {
        throw new Error("Game container or question element not found");
    }
    gameContainer.innerHTML = "";
    questionElement.textContent = question;
    answers.forEach((answer) => {
        const option = document.createElement("button");
        option.textContent = answer;
        gameContainer.appendChild(option);
    });
}
gameContainer.addEventListener("click", (event) => {
    const target = event.target; //target is an HTMLElement
    if (target.tagName === "BUTTON") {
        const selectedOption = target.textContent;
        //checking if selectedOption is not null
        if (selectedOption && selectedOption === validOption) {
            round();
        }
        else {
            alert("Wrong answer!");
        }
    }
});
function round() {
    const randomGame = Math.random() > 0.5 ? elixirGame : spellGame;
    randomGame();
}
function startGame() {
    return __awaiter(this, void 0, void 0, function* () {
        yield fetchAllData();
        round();
    });
}
startGame();
//# sourceMappingURL=game.js.map
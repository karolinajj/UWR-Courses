// wszystko
type Inventor = {
  id: string;
  firstName: string;
  lastName: string;
};

type Elixir = {
  id: string;
  name: string;
  effect: string;
  sideEffects: string | null;
  characteristics: string | null;
  time: string | null;
  difficulty: string;
  ingredients: any[];
  inventors: Inventor[];
  manufacturer: string | null;
};

type Spell = {
  id: string;
  name: string;
  incantation: string | null;
  effect: string | null;
  canBeVerbal: boolean;
  type: string;
  light: string;
  creator: string | null;
};

enum Endpoints {
  ELIXIRS = "Elixirs",
  SPELLS = "Spells",
};

let elixirs: Elixir[] = [];
let spells: Spell[] = [];

let validOption: string | undefined = undefined;

const gameContainer = document.getElementById("game")!;

async function fetchData(endpoint: Endpoints) {
  const response = await fetch(
    `https://wizard-world-api.herokuapp.com/${endpoint}`
  );
  if (!response.ok) {
    throw new Error(`Error fetching data from ${endpoint}`);
  }

  const data = await response.json();

  return data;
}
//test for fecthData:
//fetchData(Endpoints.SPELLS); //should work
//fetchData("test"); //should not work
//fetchData("Spells"); //should not work


async function fetchAllData() {
  const [elixirsResponseRaw, spellsResponseRaw] = await Promise.all([
    fetchData(Endpoints.ELIXIRS),
    fetchData(Endpoints.SPELLS),
  ]);

  const elixirsResponse = elixirsResponseRaw as Elixir[];
  const spellsResponse = spellsResponseRaw as Spell[];

  elixirs = elixirsResponse.filter((elixir: Elixir) => elixir.effect);
  spells = spellsResponse.filter((spell: Spell) => spell.incantation);
}

function getRandomElements<ArrayType>(array: ArrayType[], count: number): ArrayType[] {
  const indexes = new Set<number>();

  while (indexes.size < count) {
    const randomIndex = Math.floor(Math.random() * array.length);
    indexes.add(randomIndex);
  }

  return Array.from(indexes).map((index) => array[index]);
}

function generateOptions<T>(randomElements: T[]) {
  const [rightOption, ...rest] = randomElements;

  const options = [rightOption, ...rest].sort(() =>
    Math.random() > 0.5 ? 1 : -1
  );

  return {
    rightOption,
    options,
  };
}

function elixirGame() {
    const { options, rightOption } = generateOptions(
    getRandomElements(elixirs, 3)
  );

  validOption = rightOption.name;

  console.log(`Cheat Mode: Right answer is ${validOption}`);

  renderOptions(
    `Which elixir effect is: "${rightOption.effect}"?`,
    options.map((elixir) => elixir.name)
    );
}

function spellGame() {
    const { options, rightOption } = generateOptions(
    getRandomElements(spells, 3)
  );

  validOption = rightOption.name;

  console.log(`Cheat Mode: Right answer is ${validOption}`);

  renderOptions(
    `Which spell incantation is: "${rightOption.incantation}"?`,
    options.map((spell) => spell.name)
  );
}

function renderOptions(question: string, answers: string[]) {
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
  const target = event.target as HTMLElement; //target is an HTMLElement

  if (target.tagName === "BUTTON") {
    const selectedOption = target.textContent;

    //checking if selectedOption is not null
    if (selectedOption && selectedOption === validOption) {
      round();
    } else {
        alert("Wrong answer!");
    }
  }
});

function round() {
  const randomGame = Math.random() > 0.5 ? elixirGame : spellGame;
  
  randomGame();
}

async function startGame() {
  await fetchAllData();
  round();
}
startGame();
